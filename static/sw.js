/**
 * Sri Sri ❤️ AI CA & Global Tax Intelligence
 * Enterprise Progressive Web App (PWA) Service Worker
 * Offline Resilience & High-Performance Asset Caching
 */

const CACHE_NAME = 'sri-sri-ca-v1.2';
const STATIC_ASSETS = [
    './',
    './index.html',
    './styles.css',
    './app.js',
    './manifest.json',
    './logo.png',
    './icon-192.png',
    './icon-512.png'
];

// Install Event - Pre-cache Core Shell
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(STATIC_ASSETS).catch(err => {
                console.warn('[SW] Cache addAll partial warning:', err);
            });
        }).then(() => self.skipWaiting())
    );
});

// Activate Event - Clean old caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((name) => {
                    if (name !== CACHE_NAME) {
                        return caches.delete(name);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// Fetch Event - Stale-While-Revalidate for Static, Network-First for API
self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);

    // Skip non-GET requests
    if (event.request.method !== 'GET') {
        return;
    }

    // API calls: Network first, then fallback to empty/mock if offline
    if (url.pathname.startsWith('/api/')) {
        event.respondWith(
            fetch(event.request).catch(async () => {
                const cached = await caches.match(event.request);
                if (cached) return cached;
                return new Response(JSON.stringify({ 
                    offline: true, 
                    message: "ઓફલાઇન મોડ સક્રિય છે. સ્થાનિક ડેટા ઉપલબ્ધ છે." 
                }), {
                    headers: { 'Content-Type': 'application/json' }
                });
            })
        );
        return;
    }

    // Static assets & navigation: Cache First / Stale-While-Revalidate
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            const fetchPromise = fetch(event.request).then((networkResponse) => {
                if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
                    const responseToCache = networkResponse.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseToCache);
                    });
                }
                return networkResponse;
            }).catch(() => {
                // If network fails and no cache, fallback to index
                if (event.request.mode === 'navigate') {
                    return caches.match('/');
                }
                return cachedResponse;
            });

            return cachedResponse || fetchPromise;
        })
    );
});
