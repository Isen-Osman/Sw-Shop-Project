# 🔐 Authentication Setup Guide

## 📦 Installation

1. **Install required packages:**
```bash
pip install -r requirements.txt
```

2. **Run migrations:**
```bash
python manage.py migrate
```

3. **Create a superuser:**
```bash
python manage.py createsuperuser
```

## 🌐 Social Authentication Setup

### Google OAuth Setup

1. **Go to Google Cloud Console:**
   - Visit: https://console.cloud.google.com/
   - Create a new project or select existing one

2. **Enable Google+ API:**
   - Go to "APIs & Services" > "Library"
   - Search for "Google+ API" and enable it

3. **Create OAuth 2.0 credentials:**
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth 2.0 Client IDs"
   - Choose "Web application"
   - Add authorized redirect URIs:
     - `http://127.0.0.1:8000/accounts/google/login/callback/` (development)
     - `https://yourdomain.com/accounts/google/login/callback/` (production)

4. **Get your credentials:**
   - Copy Client ID and Client Secret

### Facebook OAuth Setup

1. **Go to Facebook Developers:**
   - Visit: https://developers.facebook.com/
   - Create a new app or select existing one

2. **Add Facebook Login:**
   - Go to "Add Product" > "Facebook Login"
   - Choose "Web" platform

3. **Configure OAuth settings:**
   - Add Valid OAuth Redirect URIs:
     - `http://127.0.0.1:8000/accounts/facebook/login/callback/` (development)
     - `https://yourdomain.com/accounts/facebook/login/callback/` (production)

4. **Get your credentials:**
   - Copy App ID and App Secret

## ⚙️ Django Admin Configuration

1. **Access Django Admin:**
   - Go to: http://127.0.0.1:8000/admin/
   - Login with your superuser credentials

2. **Add Social Applications:**
   - Go to "Sites" and add your domain:
     - Domain name: `127.0.0.1:8000` (development)
     - Display name: `Modern Shop`
   
   - Go to "Social Applications" and add:
     - **Google:**
       - Provider: Google
       - Name: Google
       - Client ID: [Your Google Client ID]
       - Secret Key: [Your Google Client Secret]
       - Sites: Select your site
     
     - **Facebook:**
       - Provider: Facebook
       - Name: Facebook
       - Client ID: [Your Facebook App ID]
       - Secret Key: [Your Facebook App Secret]
       - Sites: Select your site

## 🚀 Usage

### Available URLs:
- **Login:** `/accounts/login/`
- **Signup:** `/accounts/signup/`
- **Logout:** `/accounts/logout/`
- **Password Reset:** `/accounts/password/reset/`

### Features:
- ✅ Email/Password authentication
- ✅ Google OAuth login
- ✅ Facebook OAuth login
- ✅ Email verification
- ✅ Password reset
- ✅ Remember me functionality
- ✅ Beautiful responsive UI
- ✅ Mobile-friendly design

## 🎨 Customization

### Colors:
- **Login page:** Blue gradient
- **Signup page:** Green gradient  
- **Logout page:** Red gradient

### Styling:
- All pages use Tailwind CSS
- Responsive design
- Smooth animations
- Professional UI

## 🔧 Environment Variables (Optional)

Create a `.env` file for production:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=your-database-url
```

## 📱 Mobile Support

- Responsive design works on all devices
- Touch-friendly buttons
- Mobile-optimized forms
- Fast loading times

## 🔒 Security Features

- CSRF protection
- Email verification required
- Password strength validation
- Rate limiting on login attempts
- Secure session management
- HTTPS redirect (in production)

## 🎯 Next Steps

1. **Test the authentication flow**
2. **Customize the UI if needed**
3. **Set up email backend for production**
4. **Configure HTTPS for production**
5. **Add additional social providers if needed**

## 🆘 Troubleshooting

### Common Issues:

1. **Social login not working:**
   - Check OAuth credentials
   - Verify redirect URIs
   - Ensure APIs are enabled

2. **Email verification not sending:**
   - Check email backend settings
   - Verify SMTP configuration

3. **Styling issues:**
   - Ensure Tailwind CSS is loaded
   - Check for CSS conflicts

### Support:
- Check Django AllAuth documentation
- Review browser console for errors
- Verify all migrations are applied
