# 📦 How to Publish Your First Android APK/AAB Release on GitHub

This guide walks you through creating and publishing your app’s first downloadable Android APK/AAB release using GitHub’s Releases system.

---

## 1. **Build Your APK or AAB**

- Open the project in Android Studio.
- Run the Rust library build steps in your README:
    ```sh
    cd rust-backend
    cargo ndk -t armeabi-v7a -t arm64-v8a -o ../app/src/main/jniLibs build --release
    ```
- In Android Studio:
    - Menu: **Build > Build Bundle(s) / APK(s) > Build APK(s)** (for APK)
    - Or: **Build > Generate Signed Bundle / APK...** to generate an AAB for Play Store submission
- Find your APK/AAB in:
    - APK: `app/build/outputs/apk/release/app-release.apk`
    - AAB: `app/build/outputs/bundle/release/app-release.aab`

---

## 2. **Create a New Release on GitHub**

- Go to: https://github.com/iamomnishropbot/opnDOC/releases
- Click **Draft a new release**
- Fill in:
    - **Tag version**: `v1.0.0` or similar
    - **Release title**: e.g., `First Android APK Release`
    - **Description**: E.g.:
      > Initial release. Includes Rust-powered backend, Kotlin JNI integration, and local file persistence.

---

## 3. **Attach Your APK/AAB File**

- Drag and drop your `app-release.apk` (or `.aab`) into the release form to upload as an asset.

---

## 4. **Publish the Release**

- Click **Publish release**
- Your app is now downloadable by anyone from the Releases page!

---

## 🚀 **Optional: Automate Releases with GitHub Actions**

For future builds, you can automate APK generation and upload using GitHub Actions!
- Ask for a workflow (`.github/workflows/android-release.yml`) and we’ll set it up.

---

**For support, see:**
- [README_DEPLOY.md](https://github.com/iamomnishropbot/opnDOC/blob/main/README_DEPLOY.md)
- [Issues](https://github.com/iamomnishropbot/opnDOC/issues)

---
