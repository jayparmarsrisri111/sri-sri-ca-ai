/**
 * Sri Sri ❤️ AI CA & Global Tax Intelligence
 * Enterprise Progressive Web App (PWA) Service Worker
 * Offline Resilience & High-Performance Asset Caching
 */

const CACHE_NAME = 'sri-sri-ca-v2.0';
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

// Install Event - Pre-cache Core Shell with skipWaiting
self.addEventListener('install', (event) => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(STATIC_ASSETS).catch(err => {
                console.warn('[SW] Cache addAll partial warning:', err);
            });
        })
    );
});

// Activate Event - Clean old caches and claim clients immediately
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((name) => {
                    if (name !== CACHE_NAME) {
                        console.log('[SW] Deleting old cache:', name);
                        return caches.delete(name);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// Fetch Event - Network-First for Navigation, Network-First for API, Stale-While-Revalidate for Static
self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);

    // Skip non-GET requests
    if (event.request.method !== 'GET') {
        return;
    }

    // 1. Navigation (HTML documents): NETWORK-FIRST so live updates always show immediately
    if (event.request.mode === 'navigate') {
        event.respondWith(
            fetch(event.request).then((networkResponse) => {
                if (networkResponse && networkResponse.status === 200) {
                    const responseToCache = networkResponse.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseToCache);
                    });
                }
                return networkResponse;
            }).catch(() => {
                return caches.match(event.request).then(cached => cached || caches.match('/'));
            })
        );
        return;
    }

    // 2. API calls: Network first, then fallback to offline mock
    if (url.pathname.startsWith('/api/')) {
        event.respondWith(
            fetch(event.request).catch(async () => {
                const cached = await caches.match(event.request);
                if (cached) return cached;
                return new Response(JSON.stringify({ 
                    offline: true, 
                    message: "Offline mode active. Cached data is available." 
                }), {
                    headers: { 'Content-Type': 'application/json' }
                });
            })
        );
        return;
    }

    // 3. Static assets: Network First with Cache Fallback for CSS & JS
    if (url.pathname.endsWith('.css') || url.pathname.endsWith('.js')) {
        event.respondWith(
            fetch(event.request).then((networkResponse) => {
                if (networkResponse && networkResponse.status === 200) {
                    const responseToCache = networkResponse.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseToCache);
                    });
                }
                return networkResponse;
            }).catch(() => caches.match(event.request))
        );
        return;
    }

    // 4. Other assets (images, icons): Cache First
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            return cachedResponse || fetch(event.request).then((networkResponse) => {
                if (networkResponse && networkResponse.status === 200) {
                    const responseToCache = networkResponse.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseToCache);
                    });
                }
                return networkResponse;
            });
        })
    );
});
