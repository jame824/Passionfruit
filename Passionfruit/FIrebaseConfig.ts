// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDtNBUU7lfC86zTSilMqbmnA9Lj7F_04O8",
  authDomain: "passionfruit-3422a.firebaseapp.com",
  projectId: "passionfruit-3422a",
  storageBucket: "passionfruit-3422a.firebasestorage.app",
  messagingSenderId: "18083696070",
  appId: "1:18083696070:web:cb6010ccd62bdbe794b6c7",
  measurementId: "G-4Y756W4GL1"
};

// Initialize Firebase
export const FIREBASE_APP = initializeApp(firebaseConfig)
export const FIREBASE_AUTH = getAuth(FIREBASE_APP)
export const FIRESTORE_DB = getFirestore(FIREBASE_APP)