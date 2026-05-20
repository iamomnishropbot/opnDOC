# opnDOC Android Rust+Kotlin Backend Handoff

## Build & Deploy

### Rust Backend
1. `cd rust-backend`
2. Install cross-compile targets:
    - `rustup target add aarch64-linux-android armv7-linux-androideabi`
    - Install cargo-ndk: `cargo install cargo-ndk`
3. Build for Android:
    - `cargo ndk -t armeabi-v7a -t arm64-v8a -o ../app/src/main/jniLibs build --release`
4. Verify: `.so` files are present in `app/src/main/jniLibs/armeabi-v7a/` and `.../arm64-v8a/`

### Android Studio Project
1. Open **Android Studio (Panda 4+)**
2. Open the `app/` directory.
3. Ensure your source directory `app/src/main/java/com/iamomnishropbot/opndoc/BrainDataBridge.kt` exists as above.
4. Ensure `System.loadLibrary("rust_backend")` is present and matches your Rust crate's lib name.
5. Use as:
    ```kotlin
    val bridge = BrainDataBridge(context)
    bridge.saveBrainData(mapOf("word_fix" to mapOf("alpha" to "beta")))
    val data = bridge.loadBrainData()
    ```
6. The backend will always return a normalized schema (`word_fix`, `history_log`, and `user_profile`), handling missing keys gracefully.

### Notes
- You can extend the Rust interface with more exported functions for more features.
- For schema migration or validation, prefer letting Rust handle *all* normalization of user data.
- Your APK will support all Android architectures included in your build.
- All data is persisted as prettified JSON in internal app storage.

### Testing
- Modify and test your data on device or emulator—changes will persist as expected.
- If JNI or library not found errors occur, double-check your ABI, naming, and `.so` placement.

---

**Contact:**  
For more info or maintainership, see [https://github.com/iamomnishropbot/opnDOC](https://github.com/iamomnishropbot/opnDOC)

---

## Further Expansion

- For more complex interfaces, you can define more functions in Rust and generate bindings.
- For web/WASM, use the analogous InMemory backend or WebAssembly bindings.
- Unit test Rust logic in isolation for additional safety.

---
