/**
 * Google Analytics 4 — visit counts, geography (country/region/city), traffic sources.
 * 1. Create a property: https://analytics.google.com → Admin → Create property → Web data stream
 * 2. Copy the "Measurement ID" (format G-XXXXXXXXXX) and paste it below.
 * 3. Deploy your site; open Reports → User attributes or Realtime to see data.
 */
(function () {
  const GA4_MEASUREMENT_ID = "G-HJHX98NNMK";

  if (!GA4_MEASUREMENT_ID || !/^G-[A-Z0-9]+$/i.test(GA4_MEASUREMENT_ID)) {
    return;
  }

  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA4_MEASUREMENT_ID);
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  window.gtag = gtag;
  gtag("js", new Date());
  gtag("config", GA4_MEASUREMENT_ID);
})();
