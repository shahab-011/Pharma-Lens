# 🚀 PharmaLens Production Deployment Guide

This guide provides step-by-step instructions to deploy **PharmaLens**:
- **Backend API (FastAPI)** ➡️ **Render**
- **Frontend App (React + Vite)** ➡️ **Netlify**

---

## 🛠️ Prerequisites
1. **GitHub Repository**: Push this code to your GitHub account.
2. **Groq API Key**: Obtain a free API key from [Groq Console](https://console.groq.com/).
3. **Render Account**: Register at [render.com](https://render.com/).
4. **Netlify Account**: Register at [netlify.com](https://netlify.com/).

---

## 1️⃣ Deploying Backend to Render

### Option A: Using Render Blueprint (Automatic & Recommended)
1. Go to your **[Render Dashboard](https://dashboard.render.com/)**.
2. Click **New +** ➡️ **Blueprint**.
3. Connect your GitHub repository (`PharmaLens`).
4. Render will automatically detect `render.yaml`.
5. Under **Environment Variables**, set:
   - `GROQ_API_KEY`: `your_actual_groq_api_key`
6. Click **Apply**.
7. Once deployment finishes, copy your backend URL (e.g., `https://pharmalens-backend.onrender.com`).

---

### Option B: Manual Web Service Setup
1. Go to **Render Dashboard** ➡️ **New +** ➡️ **Web Service**.
2. Connect your repository.
3. Configure the settings:
   - **Name**: `pharmalens-backend`
   - **Environment**: `Python`
   - **Region**: Choose closest to you (e.g., Oregon)
   - **Branch**: `main` (or `master`)
   - **Root Directory**: `.`
   - **Build Command**: `python -m pip install --upgrade pip && pip install -r requirements.txt`
   - **Start Command**: `uvicorn backendd.main:app --host 0.0.0.0 --port $PORT`
4. Add **Environment Variables**:
   - `PYTHON_VERSION`: `3.12.0`
   - `GROQ_API_KEY`: `your_actual_groq_api_key`
   - `GROQ_MODEL`: `llama-3.3-70b-versatile` (or `llama-3.1-8b-instant`)
   - `CORS_ORIGINS`: `*` (or your Netlify site URL)
5. Under **Advanced Settings**:
   - **Health Check Path**: `/health`
6. Click **Create Web Service**.
7. Verify by opening `https://<your-render-app>.onrender.com/health` in your browser. You should see `{"status": "healthy", "service": "PharmaLens"}`.

---

## 2️⃣ Deploying Frontend to Netlify

1. Log in to your **[Netlify Dashboard](https://app.netlify.com/)**.
2. Click **Add new site** ➡️ **Import an existing project**.
3. Connect your GitHub provider and choose the `PharmaLens` repository.
4. Netlify will read `netlify.toml`. Confirm these build settings:
   - **Base directory**: `frontendd`
   - **Build command**: `npm run build`
   - **Publish directory**: `dist` (or `frontendd/dist`)
5. Click **Environment variables** (or **Add environment variable**):
   - **Key**: `VITE_API_URL`
   - **Value**: `https://<your-render-backend-url>.onrender.com` *(Replace with your live Render backend URL)*
6. Click **Deploy site**.
7. Once deployed, Netlify will provide your site domain (e.g., `https://pharmalens.netlify.app`).

---

## 🔒 Security & Best Practices
- **Never commit `.env` files**: All sensitive tokens like `GROQ_API_KEY` are safely ignored by `.gitignore`.
- **CORS Handling**: Backend is configured with `allow_origin_regex` to support Netlify domain names out-of-the-box.
- **SPA Fallback**: SPA routes and page refreshes are handled by `netlify.toml` and `public/_redirects`.

---

## 🧪 Local Verification Commands

### Backend:
```bash
# Run FastAPI server locally
uvicorn backendd.main:app --reload --port 8001
```

### Frontend:
```bash
cd frontendd
npm run dev
```
