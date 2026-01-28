## Simple HTTP Client for Home Assistant

> **⚠️ IMPORTANT: Integration Renamed**
>
> This integration was previously called **"Simple cURL"** (domain: `simple_curl`). It has been renamed to **"Simple HTTP Client"** (domain: `simple_http_client`).
>
> **If you're upgrading from version v1.0.0:**
>
> **For HACS users:**
> 1. Remove from `configuration.yaml`: `simple_curl:` (if present)
> 2. Restart Home Assistant to disable the old integration
> 3. In HACS → Integrations, find "Simple cURL" and remove it
> 4. Remove old repository: `https://github.com/storm1er/ha-simple-curl`
> 5. Add repository: `https://github.com/storm1er/ha-simple-http-client`
> 6. Download "Simple HTTP Client"
> 7. Restart Home Assistant
> 8. Go to **Settings** → **Devices & Services** → **Add Integration** → search for "Simple HTTP Client"
> 9. Update all service calls: `simple_curl.fetch` → `simple_http_client.fetch`
>
> **For manual installation users:**
> 1. Delete `custom_components/simple_curl/` folder
> 2. Download and extract to `custom_components/simple_http_client/`
> 3. Remove from `configuration.yaml`: `simple_curl:` (if present)
> 4. Restart Home Assistant
> 5. Go to **Settings** → **Devices & Services** → **Add Integration** → search for "Simple HTTP Client"
> 6. Update all service calls: `simple_curl.fetch` → `simple_http_client.fetch`

A lightweight custom integration that provides a callable service to fetch URLs with custom HTTP methods and headers, returning the response as a variable for use in automations and scripts.

### Installation

After downloading from HACS, add to your `configuration.yaml`:

```yaml
simple_http_client:
```

Then restart Home Assistant. The service will be available immediately.

### Features

- Minimal configuration - just add to configuration.yaml
- Fetch any URL with custom HTTP methods (GET, POST, PUT, PATCH, DELETE, etc.)
- Set custom headers and request body
- Response data stored in variables using `response_variable`
- Returns status code, content, and response headers
- Built-in error handling

### Quick Example

```yaml
automation:
  - alias: "Fetch API Data"
    trigger:
      - platform: time
        at: "09:00:00"
    action:
      - service: simple_http_client.fetch
        data:
          url: "https://api.example.com/data"
          method: "GET"
          headers:
            Authorization: "Bearer token"
        response_variable: api_response

      - service: notify.notify
        data:
          message: "API returned: {{ api_response.content }}"
```

### Service: `simple_http_client.fetch`

**Parameters:**
- `url` (required): The URL to fetch
- `method` (optional): HTTP method (default: GET)
- `headers` (optional): HTTP headers as key-value pairs
- `body` (optional): Request body content
- `timeout` (optional): Timeout in seconds (default: 10)

**Returns:**
- `status`: HTTP status code
- `content`: Response body as text
- `headers`: Response headers
- `error`: Error message (if failed)

For detailed documentation and more examples, see the [GitHub repository](https://github.com/storm1er/ha-simple-http-client).
