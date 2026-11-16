# FPT Shop CDP / Marketing Tracking Audit

Thoi gian inspect: 2026-06-04, qua Chrome DevTools MCP tren tab FPT Shop dang mo.  
Pham vi thao tac da bat duoc: page view, vao category dien thoai/laptop, chon san pham/variant, scroll, xem media, them gio hang, toggle gio hang, chon khuyen mai, voucher/loyalty/promotion checks.  
Gia tri nhay cam nhu so dien thoai, token, refresh token, session value, cookie value da duoc redacted; bao cao chi ghi ten field/key.

## Tom tat nhanh

FPT Shop thu thap du lieu qua hai nhom chinh:

1. First-party FPT:
   - `papi.fptshop.com.vn` cho login/order/cart/promotion/loyalty/comment/profile.
   - `octopus-stream01-cads.fpt.vn/com.fpt/301` qua Snowplow `https://fptshop.com.vn/script/sp.js`.
   - `fptshop.com.vn/cdn-cgi/rum` qua Cloudflare RUM.

2. Ben thu ba:
   - Insider: `fptshop.api.useinsider.com/ins.js?id=10001396`, `hit.api.useinsider.com`, `carrier.useinsider.com`, `unification.useinsider.com`, `falcon.useinsider.com`, `abacus.api.useinsider.com`.
   - Google/GA4/Google Ads: `analytics.google.com/g/collect`, `googleadservices.com`, `doubleclick.net`, `googletagmanager.com`.
   - Meta Pixel: `connect.facebook.net/en_US/fbevents.js`, `facebook.com/tr/`, `facebook.com/privacy_sandbox/pixel/register/trigger`.
   - TikTok Pixel: `analytics.tiktok.com/i18n/pixel/static/main...js`, `analytics.tiktok.com/api/v2/pixel*`.
   - Admicro/VC Corp: `static.amcdn.vn/core/adm_tracking.js`, `amcdn.vn/anlz`, `lg1.logging.admicro.vn/_tracking1.gif`, `static.contineljs.com/cpa/core/tp2_core.min.js`.
   - Retargeting / ad sync khac: `asia.creativecdn.com`, `sync.taboola.com`, `tg.socdm.com`, `s-cs.send.microad.jp`, `casalemedia.com`.

Snapshot cuoi ghi nhan 1,202 su kien recorder:
`669 storage.setItem`, `258 cookie.set`, `121 image pixel`, `62 fetch`, `51 xhr`, `40 beacon`.

## File / source quan trong

### 1. FPT Snowplow collector

Source: `https://fptshop.com.vn/script/sp.js`

Bang chung trong source:
- File la Snowplow web analytics v3.16.0.
- Co `newTracker`, `trackPageView`, `trackSelfDescribingEvent`.
- Co `trackAddToCart` voi schema `iglu:com.snowplowanalytics.snowplow/add_to_cart/jsonschema/1-0-0`.
- Payload tu source them cac truong: `vp`, `ds`, `vid`, `sid`, `duid`, `uid`, `refr`, `url`, `cx`, `ue_px`.

Endpoint observed:
- `POST https://octopus-stream01-cads.fpt.vn/com.fpt/301`

Field observed:
- Dinh danh / session: `eid`, `cookie`, `vid`, `sid`, `duid`, `uid`, `_sp_id.d55b`, `_sp_ses.d55b`.
- Ngu canh hanh vi: `e`, `tv`, `tna`, `aid`, `p`, `url`, `refr`, `lang`, `res`, `cd`, `tz`, `dtm`, `vp`, `ds`, `stm`.
- Event custom: `ue_px`.
- Context: `cx`.

### 2. FPT frontend API client / cart / order

Source: `https://fptshop.com.vn/_next/static/chunks/73463-0c09a56ee1026a51.js`

Bang chung trong source:
- Chua client API cho `BFF_ORDER`, `FULLTEXT_SEARCH_SERVICE`, `AUTH`, `STORE_FRONT`.
- Doc cookie `token`, `refreshToken`, gan `Authorization`.
- Set header `order-channel`.
- Chua endpoint `cart`, `cart/count-item`, `cart/selected-promotion`, `cart/toggle-item`, `voucher`, `loyalty/point`, `comment`, `customer/profile`, `order`.

Endpoint observed:
- `POST https://papi.fptshop.com.vn/gw/v1/public/bff-order/cart`
- `GET https://papi.fptshop.com.vn/gw/v1/public/bff-order/cart/count-item`
- `POST https://papi.fptshop.com.vn/gw/v1/public/bff-order/cart/selected-promotion`
- `POST https://papi.fptshop.com.vn/gw/v1/public/bff-order/cart/toggle-item`
- `POST https://papi.fptshop.com.vn/gw/v1/private/bff-order/voucher`
- `GET https://papi.fptshop.com.vn/gw/v1/private/bff-order/loyalty/point`
- `POST https://papi.fptshop.com.vn/gw/v1/public/fulltext-search-service/product-by-upcs`
- `POST https://papi.fptshop.com.vn/gw/v1/public/bff-order/cart/product-combo`

Field dinh danh observed:
- `phoneNumber`
- `sessionId`
- `cartSessionId` trong localStorage
- `token`, `refreshToken`, `Authorization`
- `order-channel`
- `oidc.*`
- `userLocation`

Field hanh vi / thuong mai observed:
- Cart add: `cartItem.itemCart`, `cartItem.quantity`, `cartItem.unitCode`, `cartItem.type`, `orderType`, `orderAttribute`.
- Cart toggle: `ids`, `shopCode`, `shipmentPrice`.
- Promotion: `promotions[0].code`, `promotions[0].status`, `promotions[0].productId`.
- Product lookup: `upcs`, `isExcludedProduct`, `sku`.
- Warranty/combo: `data[0].sku`, `data[0].price`, `data[0].warrantyMonthDefault`, `mainItemCode`, `itemComboCodes`, `phaseId`.
- Voucher/loyalty: `skipCount`, `maxResultCount`, `types`, `status`, `voucherChannels`, loyalty point response.

Response gio hang con tra ve metadata marketing/commerce:
- Product: `sku`, `name`, `brandId`, `sectorId`, `typeId`, `industryId`, `productTypeId`, `productGroupId`, `upcCode`, `slug`, `upcSlug`, `variants`, `color`.
- Gia: `price`, `discount`, `priceAfterDiscount`, `total`, `totalBill`, `calculatorPrice`.
- Khuyen mai: `promotions[].code`, `programType`, `statusCode`, `vouchers[]`, `paymentPromotions[]`.

### 3. Insider CDP / marketing automation

Source: `https://fptshop.api.useinsider.com/ins.js?id=10001396`

Bang chung trong source:
- `partner.name = fptshop`, `pId = 10001396`.
- `dataCollectStatus: true`.
- `UCDCartCollectionStatus: true`.
- `UCDBrowseAbandonmentCollectionStatus: true`.
- `eventCollectionStatus`: category, product, cart, purchase, other page dang bat.
- Co logic lead form dua `name`, `phone_number`, `email`, `gdpr`, `user_id`, `variation_id`, `source`, `platform` len `falcon.useinsider.com/.../lead-sender`.

Endpoint observed:
- `POST https://hit.api.useinsider.com/hit`
- `POST https://falcon.useinsider.com/api/v2/log-tracking/hit/fptshop`
- `POST https://carrier.useinsider.com/v2/contact/ucd/update`
- `POST https://unification.useinsider.com/api/event/v1/insert`
- `POST https://abacus.api.useinsider.com/set-basket-stats`

Field observed:
- Dinh danh: `spUID`, `insider_id`, `user_id`, `insUserInfoHash`, `ins-gaSSId`, `ins-lead-spuid`, `partner`, `source`.
- Hanh vi: `events[0].event_name`, `timestamp`, `event_params.pid`, `event_params.na`, `event_params.cu`, `event_params.up`, `event_params.url`, `event_params.piu`, `event_params.qu`, `event_params.sid`, `event_params.ta`.
- Cart / browse abandonment storage: `ins-cart-product-list`, `total-cart-amount`, `paid-products`, `ins-ucd-cart-collection-hash`, `ins-ucd-last-browsed-items`, `ins-last-viewed-prod-*`, `ins-product-visit-count`, `ins-categories-visit-count`.
- Campaign state: `sp-camp-c861`, `sp-goal-c861-140`, `ins-user-segments`, `ins-journey-camp-454`, `ins-wp-*`.

### 4. Meta Pixel

Source: `https://connect.facebook.net/en_US/fbevents.js`

Endpoint observed:
- `POST https://www.facebook.com/tr/`
- `GET https://www.facebook.com/privacy_sandbox/pixel/register/trigger/`

Field observed:
- Dinh danh: `id` pixel, `_fbp` / `fbp`, `cudff[ph]` (phone-derived signal label/value was masked by DevTools output), `cs_est`.
- Page/product: `dl`, `rl`, `pmd[title]`, `pmd[locale]`, `pmd[description]`, `pmd[keywords]`, `pmd[contents]`, product ids/name/brand/price/availability.
- Interaction: `ev`, `cd[buttonFeatures]`, `cd[buttonText]`, `cd[formFeatures]`, `cd[pageFeatures]`, `cd[parameters]`.
- Device/context: `sw`, `sh`, `ts`, `tz`, `plt`.

### 5. TikTok Pixel

Source: `https://analytics.tiktok.com/i18n/pixel/static/main.MTc5ZjUxNDU4MQ.js`

Endpoint observed:
- `POST https://analytics.tiktok.com/api/v2/pixel`
- `POST https://analytics.tiktok.com/api/v2/pixel/act`
- `POST https://analytics.tiktok.com/api/v2/pixel/inter`

Field observed:
- Dinh danh: `context.user.anonymous_id`, `context.pixel.code`, `context.session_id`, `context.pageview_id`, `context.csid`, `context.page_csid`, cookie `ttcsid`, `ttcsid_<pixel>`, `_ttp`.
- Diagnostic identity labels: `raw_email`, `raw_phone`, `hashed_email`, `hashed_phone` labels (khong ghi value).
- Page/action: `event`, `action`, `context.page.url`, `context.page.referrer`, `auto_collected_properties.page_trigger`, `trigger_element.tag`, `trigger_element.attributes.class`, `trigger_element.inner_text`, `trigger_element.xpath`, `trigger_element.position.x/y`.
- Scroll/interaction metrics: `auto_collected_properties.page_inter.*`, `inter.ct`, `inter.st`.

### 6. Google Analytics / Google Ads

Source:
- `https://www.googletagmanager.com/gtag/js?id=G-ZR815NQ85K`
- `https://www.googletagmanager.com/gtag/js?id=AW-16972417338`
- `https://www.googletagmanager.com/gtag/js?id=AW-11391348874`

Endpoint observed:
- `POST https://analytics.google.com/g/collect`
- `GET https://www.googleadservices.com/pagead/conversion/...`
- `POST https://googleads.g.doubleclick.net/pagead/viewthroughconversion/...`
- `GET https://www.google.com.vn/ads/ga-audiences`

Field observed:
- Dinh danh: `cid`, `sid`, `_ga`, `_ga_ZR815NQ85K`, `_gcl_au`, `auid`, conversion `em`/`emd` style enhanced-conversion fields.
- Event: `en=page_view`, `en=view_item`, `en=product_detail_views__after_click_on_pro`, conversion labels.
- Product: `pr1` encodes product id/name/price/quantity/variant/category.
- Page/device: `dl`, `dr`, `dt`, `sr`, `uap`, `uapv`, `uafvl`, `ul`, `uaa`, `uab`, `uamb`, `uaw`.
- Element/click context in Ads: `ec_m`, `ec_sel`, `ec_meta`, `ec_lat`, `ec_mode`.

### 7. Admicro / VC Corp tracking

Source: `https://static.amcdn.vn/core/adm_tracking.js`

Endpoint observed:
- `GET https://lg1.logging.admicro.vn/_tracking1.gif`
- `GET https://amcdn.vn/anlz`
- `GET https://lg1.logging.admicro.vn/rtg_bn`

Field observed:
- Dinh danh: `__uidac`, `__uif`, `__uid`, `__create`, `ui`, `dg`.
- Page/device: `sr`, `sc`, `hn`, `p`, `r`, `fl`, `je`, `ce`, `lc`, `cr`.
- Hanh vi: scroll position/counter trong field `i` va `sl`, time-on-site / view events.

### 8. Other ad/retargeting channels

Observed:
- `POST https://asia.creativecdn.com/tags/v2` qua `tags.creativecdn.com/...js`.
  - Fields: `v`, `sr`, `su`, `th`, `tags[0].eventType`, `tags[0].offerId`, `type`.
- `sync.taboola.com`, `tg.socdm.com`, `s-cs.send.microad.jp`, `dsum-sec.casalemedia.com`.
  - Chu yeu la cookie/user sync/retargeting; khong du payload chi tiet trong recorder.

## Storage / Cookies / Session observed

Cookies observed (ten only):
- FPT/Auth: `token`, `refreshToken`, `fptshop_cookie_consent`.
- Snowplow: `_sp_id.d55b`, `_sp_ses.d55b`.
- GA/Ads: `_ga`, `_ga_ZR815NQ85K`, `_gid`, `_gcl_au`.
- Meta: `_fbp`.
- TikTok: `_tt_enable_cookie`, `_ttp`, `ttcsid`, `ttcsid_CATS4RRC77U5NQUHEKG0`.
- Hotjar: `_hjSessionUser_731679`, `_hjSession_731679`.
- Admicro: `__uidac`, `__uif`, `__admUTMtime`, `__iid`, `__su`, `__tb`, `__IP`, `__RC`, `__R`.
- RTBHouse: `__rtbh.lid`.

localStorage/sessionStorage notable keys:
- FPT/session: `cartSessionId`, `oidc.*`, `userLocation`, `viewedProducts`, `location-storage-v2*`.
- Snowplow: `snowplowOutQueue_snowplow_dc5_post2`, `snowplowOutQueue_snowplow_dc5_post2.expires`.
- Insider: `spUID`, `insUserInfoHash`, `ins-gaSSId`, `ins-user-segments`, `insCustomAttributes`, `ins-default-attributes`, `ins-cart-product-list`, `total-cart-amount`, `paid-products`, `ins-ucd-cart-collection-hash`, `ins-ucd-last-browsed-items`, `ins-last-viewed-prod-*`, `ins-product-visit-count`, `ins-categories-visit-count`, `ins-wp-*`.
- TikTok: `tt_appInfo`, `tt_sessionId`, `tt_pixel_session_index`.
- RTBHouse: `__rtbh.lid`.
- OneSignal: `onesignal-notification-prompt`, `onesignal-pageview-count`.

## Nhan dinh CDP / automation marketing

FPT Shop dang co day du tin hieu de phuc vu CDP va automation marketing:

- Identity stitching: phone login/order (`phoneNumber`), `token`/`refreshToken`, `sessionId`, `cartSessionId`, Snowplow `duid/sid/uid`, Insider `spUID/insider_id/user_id`, GA `cid/sid`, Meta `_fbp`, TikTok anonymous/session ids, Admicro `__uid`.
- Behavioral profiling: category/product views, SKU/UPC/variant, price/discount, click button/banner/product card, scroll, page duration/interaction, referrer, source URL, product visit count, category visit count.
- Cart abandonment: Insider explicitly bat `UCDCartCollectionStatus` va luu `ins-cart-product-list`, `total-cart-amount`, `ins-ucd-cart-collection-hash`; FPT API gui `phoneNumber + sessionId + cartItem`.
- Browse abandonment: Insider bat `UCDBrowseAbandonmentCollectionStatus`, luu `ins-last-viewed-prod-*`, `ins-ucd-last-browsed-items`, `ins-product-visit-count`.
- Retargeting/ad activation: Meta/TikTok/Google Ads/Admicro/CreativeCDN nhan page, product, button/click, screen/device, referrer va conversion/cart/product event.

## Luu y gioi han

- Khong doc truc tiep HttpOnly cookies; chi thay cookie non-HttpOnly qua page JS va headers da redacted trong DevTools.
- Cac file JS phan lon minified; line number cua chunk Next/Insider co the nam tren line 1, nhung call stack va endpoint khop voi request observed.
- Neu can xac minh comment form, can thao tac gui comment that su; trong lan inspect nay minh thay source co endpoint `comment*` nhung khong thay payload comment POST trong final recorder.
