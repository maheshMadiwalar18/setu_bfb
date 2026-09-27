import { initializeApp, getApps, getApp, type FirebaseApp } from "firebase/app";
import { getAnalytics, isSupported } from "firebase/analytics";
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut, type Auth } from "firebase/auth";

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY || "",
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN || "",
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID || "",
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET || "",
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID || "",
  appId: import.meta.env.VITE_FIREBASE_APP_ID || "",
  measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID || ""
};

const looksLikeRealApiKey = /^AIza[0-9A-Za-z_-]{20,}$/.test(firebaseConfig.apiKey);
export const isFirebaseConfigured = looksLikeRealApiKey;

let app: FirebaseApp | null = null;
let auth: Auth | null = null;
let analytics: ReturnType<typeof getAnalytics> | null = null;
const googleProvider = new GoogleAuthProvider();

function getFirebaseAuth(): Auth | null {
  if (!isFirebaseConfigured) return null;
  if (auth) return auth;

  try {
    app = getApps().length ? getApp() : initializeApp(firebaseConfig);
    auth = getAuth(app);

    if (typeof window !== "undefined" && firebaseConfig.measurementId) {
      isSupported()
        .then((supported) => {
          if (supported && app) analytics = getAnalytics(app);
        })
        .catch(() => undefined);
    }
  } catch (error) {
    console.warn("Firebase is not available; continuing without Google sign-in.", error);
    app = null;
    auth = null;
  }

  return auth;
}

export const loginWithGoogle = async () => {
  const firebaseAuth = getFirebaseAuth();
  if (!firebaseAuth) {
    throw new Error("Google sign-in is not configured. Add a valid VITE_FIREBASE_API_KEY in frontend/.env");
  }
  const result = await signInWithPopup(firebaseAuth, googleProvider);
  return result.user;
};

export const logout = async () => {
  const firebaseAuth = getFirebaseAuth();
  if (!firebaseAuth) return;
  await signOut(firebaseAuth);
};

export { app, analytics, auth };
