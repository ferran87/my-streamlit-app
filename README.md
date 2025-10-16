# Website Tracking Event Analyzer

Tools to help you identify tracking events triggered by customer actions on websites using Cursor.

## 🚀 Quick Start

### Option 1: Simple Analysis (No Browser Required)
Best for quick analysis without installing browser drivers.

```bash
pip install requests beautifulsoup4 lxml
python simple_tracking_checker.py
```

### Option 2: Full Analysis (With Browser Automation)
More comprehensive analysis including real-time network monitoring.

```bash
pip install -r requirements.txt
# Install ChromeDriver: https://chromedriver.chromium.org/
python website_tracking_analyzer.py
```

## 📋 What These Tools Do

### ✅ Detects Analytics Tools
- **Google Analytics** / Google Tag Manager
- **Facebook Pixel**
- **Adobe Analytics**
- **Mixpanel**, **Amplitude**, **Segment**
- **Hotjar**, **FullStory**, **LogRocket**
- **Intercom**, **Heap**, **Klaviyo**

### ✅ Finds Tracking Events
- Click tracking on buttons/links
- Form submission tracking
- Page view events
- Custom event triggers
- E-commerce tracking (add to cart, checkout)

### ✅ Identifies Tracking Methods
- **JavaScript event calls** (`gtag()`, `fbq()`, custom functions)
- **Tracking pixels** (1x1 images)
- **Data attributes** (`data-track`, `data-analytics`)
- **HTML event handlers** (`onclick`, `onsubmit`)
- **Hidden form fields** (UTM parameters, campaign tracking)

## 🛠️ Usage Examples

### Basic Website Analysis
```python
from simple_tracking_checker import quick_tracking_analysis

results = quick_tracking_analysis("https://example.com")
```

### Analyze Specific User Actions
```python
# Define actions you want to test
actions = [
    {
        'action': 'click',
        'selector': '#buy-now-button',
        'description': 'Purchase button click'
    },
    {
        'action': 'submit', 
        'selector': '#newsletter-form',
        'description': 'Newsletter signup'
    }
]

# Analyze with browser automation
from website_tracking_analyzer import WebsiteTrackingAnalyzer

analyzer = WebsiteTrackingAnalyzer()
results = analyzer.analyze_page_interactions("https://example.com", actions)
```

## 📊 Sample Output

```
🔍 TRACKING ANALYSIS for https://example.com
============================================================

📊 ANALYTICS TOOLS DETECTED: 3
  ✓ Google Analytics/GTM
  ✓ Facebook Pixel
  ✓ Hotjar

🔧 TRACKING EVENT PATTERNS: 2
  ✓ Google Analytics Events: 15 matches
    - gtag('event'
    - dataLayer.push
    - ga('send', 'event'
  ✓ Facebook Events: 8 matches
    - fbq('track'
    - fbq('trackCustom'

🎯 ELEMENTS WITH TRACKING ATTRIBUTES: 7
  ✓ <button> with ['onclick', 'data-track']
  ✓ <a> with ['data-analytics']
  ✓ <form> with ['onsubmit']
```

## 🔍 Analysis Methods

### 1. Static Code Analysis
- Scans HTML source code
- Identifies tracking scripts and pixels
- Finds elements with tracking attributes
- **Pros**: Fast, no browser required
- **Cons**: Misses dynamically loaded tracking

### 2. Browser Network Monitoring
- Uses Selenium to simulate user actions
- Captures actual network requests
- Monitors real tracking events
- **Pros**: Sees all tracking activity
- **Cons**: Requires browser setup

### 3. JavaScript Pattern Detection
- Analyzes JavaScript code for tracking patterns
- Identifies event tracking functions
- Maps tracking to user actions
- **Pros**: Understands tracking logic
- **Cons**: Limited to visible source code

## 🎯 Common Use Cases

### E-commerce Tracking
```python
# Analyze shopping funnel tracking
actions = [
    {'selector': '.product-link', 'action': 'click', 'description': 'Product view'},
    {'selector': '.add-to-cart', 'action': 'click', 'description': 'Add to cart'},
    {'selector': '.checkout-btn', 'action': 'click', 'description': 'Checkout start'},
    {'selector': '#purchase-form', 'action': 'submit', 'description': 'Purchase complete'}
]
```

### Lead Generation
```python
# Analyze lead capture tracking
actions = [
    {'selector': '#contact-form', 'action': 'submit', 'description': 'Contact form'},
    {'selector': '.newsletter-signup', 'action': 'submit', 'description': 'Newsletter'},
    {'selector': '.download-btn', 'action': 'click', 'description': 'File download'}
]
```

### Content Engagement
```python
# Analyze content interaction tracking
actions = [
    {'selector': '.video-play', 'action': 'click', 'description': 'Video play'},
    {'selector': '.share-button', 'action': 'click', 'description': 'Social share'},
    {'selector': '.comment-form', 'action': 'submit', 'description': 'Comment post'}
]
```

## 🔧 Browser Developer Tools Method

For manual analysis, you can also use browser dev tools:

1. **Open website** in Chrome/Firefox
2. **Press F12** → Go to **Network** tab
3. **Filter by XHR/Fetch** requests
4. **Perform the customer action** you want to analyze
5. **Look for tracking requests** to analytics domains
6. **Examine request parameters** to understand what data is being sent

### Common Tracking Domains to Look For:
- `google-analytics.com`, `googletagmanager.com`
- `facebook.com`, `connect.facebook.net`
- `mixpanel.com`, `amplitude.com`
- `hotjar.com`, `fullstory.com`

## 📝 Reports and Output

### Generated Files:
- **`tracking_analysis_report.md`** - Human-readable analysis report
- **`tracking_analysis_data.json`** - Raw data for further processing
- **`tracking_analysis_[domain].json`** - Domain-specific results

### Report Sections:
1. **Analytics Tools Detected** - Which tracking platforms are in use
2. **Tracking Events Found** - Specific events triggered by actions
3. **Static Analysis Results** - Tracking found in source code
4. **Network Requests** - Actual tracking calls made
5. **Recommendations** - Insights about tracking implementation

## ⚡ Tips for Better Analysis

### 1. **Check Multiple Pages**
Different pages may have different tracking setups:
```python
pages_to_check = [
    "https://example.com",
    "https://example.com/product/123", 
    "https://example.com/checkout",
    "https://example.com/thank-you"
]
```

### 2. **Test Different User Scenarios**
- New visitor vs returning customer
- Mobile vs desktop
- Different product categories

### 3. **Look for Dynamic Tracking**
Some tracking loads conditionally:
- After user scrolls
- After time delay
- Based on user behavior

### 4. **Check for A/B Testing**
- Multiple tracking implementations
- Conditional event firing
- Different tracking for test groups

## 🚨 Privacy and Legal Notes

- **Respect robots.txt** and terms of service
- **Don't overload servers** with requests
- **Be aware of privacy laws** (GDPR, CCPA) when analyzing tracking
- **Use for legitimate purposes** like compliance audits or competitive research

## 🛠️ Troubleshooting

### Common Issues:

**"ChromeDriver not found"**
```bash
# Install ChromeDriver
# Download from: https://chromedriver.chromium.org/
# Or use: brew install chromedriver (macOS)
```

**"Element not found"**
- Check if selector is correct
- Website might be using dynamic loading
- Try waiting longer or using different selectors

**"No tracking detected"**
- Some tracking is loaded asynchronously
- Try the browser automation method
- Check for single-page applications (SPAs)

**"SSL Certificate errors"**
```python
# Add to requests
requests.get(url, verify=False)
```

## 🤝 Contributing

Feel free to enhance these tools:
- Add support for more analytics platforms
- Improve tracking pattern detection
- Add mobile app tracking analysis
- Create visualization tools for tracking flows

---

## 📚 Learn More

- [Google Analytics Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/v1)
- [Facebook Pixel Implementation](https://developers.facebook.com/docs/facebook-pixel/)
- [Adobe Analytics Implementation](https://experienceleague.adobe.com/docs/analytics/implementation/home.html)
- [GDPR Compliance for Tracking](https://gdpr-info.eu/) #   m y - s t r e a m l i t - a p p  
 