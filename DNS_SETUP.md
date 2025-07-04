# DNS Configuration for abdikamalov.com on Namecheap

## Step-by-Step Instructions

### 1. Log into Namecheap
- Go to https://www.namecheap.com
- Sign in to your account
- Go to Dashboard → Domain List
- Click "Manage" next to abdikamalov.com

### 2. Configure DNS Records

In the "Advanced DNS" tab, add these records:

#### A Records (for apex domain)
Add these four A records for GitHub Pages:

| Type | Host | Value | TTL |
|------|------|-------|-----|
| A Record | @ | 185.199.108.153 | Automatic |
| A Record | @ | 185.199.109.153 | Automatic |
| A Record | @ | 185.199.110.153 | Automatic |
| A Record | @ | 185.199.111.153 | Automatic |

#### CNAME Record (for www subdomain)
| Type | Host | Value | TTL |
|------|------|-------|-----|
| CNAME Record | www | beknazar.github.io | Automatic |

### 3. Remove Conflicting Records
- Delete any existing A records pointing to Namecheap parking page
- Delete any CNAME records for @ (if present)

### 4. Wait for DNS Propagation
- DNS changes can take 30 minutes to 48 hours to propagate
- You can check propagation status at: https://www.whatsmydns.net/

### 5. Enable HTTPS in GitHub
Once DNS propagates:
1. Go to https://github.com/beknazar/abdikamalov-website/settings/pages
2. Under "Custom domain", you should see "abdikamalov.com" 
3. Check "Enforce HTTPS" when it becomes available

## Verification
After setup, your site will be accessible at:
- https://abdikamalov.com
- https://www.abdikamalov.com

Both will redirect to the HTTPS version automatically once configured.