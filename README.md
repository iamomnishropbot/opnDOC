# opnDOC

**opnDOC** is an open-source Android application featuring a persistent, schema-normalized “Brain” powered by a high-performance Rust backend, with a modern UI built in Kotlin and Jetpack Compose.

---

## 🚀 Overview

- **Native Rust backend:** Ultra-fast, reliable data normalization and persistence across app launches.
- **JNI bridge:** Type-safe, robust Rust ⇄ Kotlin communication.
- **Jetpack Compose UI:** Modern, reactive interface with history log, CRUD and more.
- **Local file storage:** All user data is safely sandboxed (`realai_brain.json`).
- **Seamless Android build:** Easy integration with Android Studio (Panda 4+), NDK, and Rust via `cargo-ndk`.

---

## 🏗️ Features

- Instant save/load of structured data without server roundtrips.
- Schema auto-normalization (never corrupts user data).
- Full control: Extend both the Rust interface and Compose UI.
- Flexible history log, word-fix dictionary, and user profile managed natively.

---

## 📦 Quick Start

### 1. Clone & Install Requirements

```bash
git clone https://github.com/iamomnishropbot/opnDOC.git
cd opnDOC
```

- Make sure you have:
    - **Android Studio (Giraffe 3.0+ / Panda 4+)**
    - **Rust (1.72+)**, `cargo install cargo-ndk`
    - NDK installed (`ndk.dir` in `local.properties`)

### 2. Build the Rust Backend

```bash
cd rust-backend
rustup target add aarch64-linux-android armv7-linux-androideabi
cargo install cargo-ndk
cargo ndk -t armeabi-v7a -t arm64-v8a -o ../app/src/main/jniLibs build --release
```
- The `.so` libraries appear in `app/src/main/jniLibs/*`
- This powers all persistent data functions in the app.

### 3. Open in Android Studio & Sync Gradle

- Open the `opnDOC` folder in Android Studio.
- Verify `local.properties` paths for SDK and NDK.
- Sync Gradle: it should pick up the Rust libraries in `jniLibs`.

### 4. Run the App

- Hit **Run** (or `Shift+F10`)!
- The Jetpack Compose UI appears, backed by your live Rust backend.

---

## 🖼️ Main Components

### Jetpack Compose UI
- Modern android interface, including:
    - **History Log Viewer & Editor**
    - Add/delete entries with state persisted instantly
    - Fully reactive Compose components

### Rust Backend (`rust-backend`)
- Serde-based schema for:
    - `history_log: Vec<String>`
    - `word_fix: HashMap<String, String>`
    - `user_profile: HashMap<String, String>`
- Exposed to Kotlin via JNI (`BrainDataBridge.kt`)
- All data stored as pretty JSON in app sandbox

### JNI Bridge (Kotlin)
- Easy API: just call `loadBrainData()` and `saveBrainData(map)` from your Compose UI

---

## 🧑‍💻 Example Usage

Here’s the essence of working with persistent data in Compose:

```kotlin
val bridge = BrainDataBridge(context)
val brainData = bridge.loadBrainData() // returns Map<String, Any>
bridge.saveBrainData(updatedDataMap)
```

---

## 🛠️ Jetpack Compose Example

```kotlin
@Composable
fun BrainHistoryScreen(bridge: BrainDataBridge) {
    var history by remember { mutableStateOf(listOf<String>()) }
    // ... see MainActivity for full usage (list/add entries)
}
```

See `MainActivity.kt` in the app module for production patterns.

---

## 🏁 Releasing Your APK/AAB

- Manual releases: See [RELEASE_INSTRUCTIONS.md](RELEASE_INSTRUCTIONS.md)
- Tag a release and upload the APK/AAB built from Android Studio!
- Coming soon: GitHub Actions workflow for CI/CD builds

---

## 🤝 Contributing

Open source, PRs welcome!  
See [README_DEPLOY.md](README_DEPLOY.md) and [RELEASE_INSTRUCTIONS.md](RELEASE_INSTRUCTIONS.md) for dev flow.

---

## ⚖️ License

MIT License. See [LICENSE](LICENSE).

---

## 📚 Key Files

- [README_DEPLOY.md](README_DEPLOY.md) — Detailed build/deploy guide
- [RELEASE_INSTRUCTIONS.md](RELEASE_INSTRUCTIONS.md) — Ship your first APK/AAB on GitHub
- [rust-backend/src/lib.rs](rust-backend/src/lib.rs) — Rust backend logic
- [app/src/main/java/com/iamomnishropbot/opndoc/BrainDataBridge.kt](app/src/main/java/com/iamomnishropbot/opndoc/BrainDataBridge.kt)
- [app/src/main/java/com/iamomnishropbot/opndoc/MainActivity.kt](app/src/main/java/com/iamomnishropbot/opndoc/MainActivity.kt) — Compose UI

---

**Built for builders. Designed for hackability. Powered by Rust + Kotlin.**
