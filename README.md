# flet-webview-all — Test Builds

Sample application used to test [`flet-webview-all`](https://github.com/zaim-tech/flet-webview-all),
a unified webview control for the [Flet](https://flet.dev) framework, across
every platform it supports.

- **Control repository:** [github.com/zaim-tech/flet-webview-all](https://github.com/zaim-tech/flet-webview-all)
- **Documentation:** [zaim-tech.github.io/flet-webview-all](https://zaim-tech.github.io/flet-webview-all)

## Downloads

The builds below were produced by a single CI run
([Actions run 33524756815](https://github.com/zaim-tech/webviewalltest/actions/runs/33524756815))
across all supported targets: desktop, mobile, and web.

| Platform | Artifact |
| --- | --- |
| Windows | [Download](https://github.com/zaim-tech/webviewalltest/actions/runs/33524756815/artifacts/9807441770) |
| Linux | [Download](https://github.com/zaim-tech/webviewalltest/actions/runs/33524756815/artifacts/9807385294) |
| macOS | [Download](https://github.com/zaim-tech/webviewalltest/actions/runs/33524756815/artifacts/9807426966) |
| Android (APK) | [Download](https://github.com/zaim-tech/webviewalltest/actions/runs/33524756815/artifacts/9807570743) |
| Web | [Download](https://github.com/zaim-tech/webviewalltest/actions/runs/33524756815/artifacts/9807392395) |
| iOS (IPA) | [Download](https://github.com/zaim-tech/webviewalltest/actions/runs/33524756815/artifacts/9807489993) |
| iOS Simulator | [Download](https://github.com/zaim-tech/webviewalltest/actions/runs/33524756815/artifacts/9807499550) |

> [!NOTE]
> GitHub Actions artifacts require you to be **signed in to GitHub** to
> download, and they expire after the repository's configured retention
> period (90 days by default). If a link 404s, check whether the run has
> aged out and trigger a fresh build from the
> [Actions tab](https://github.com/zaim-tech/webviewalltest/actions).

## What this tests

Each artifact is the same Flet application built for its target platform,
exercising the full surface of the `flet-webview-all` control:

- Loading a remote URL and inline HTML
- JavaScript execution and the JavaScript-channel bridge
- Navigation policy (`allow_navigation`) and browser-style back/forward
- Zoom, custom user agent, and background color
- Scrolling and scroll-position events
- Console message capture and platform-native debugging (see
  [Debugging & DevTools](https://zaim-tech.github.io/flet-webview-all/guides/debugging/))
- Camera/microphone permission requests (see
  [Permissions](https://zaim-tech.github.io/flet-webview-all/guides/permissions/))

## Installing a build

**Windows / Linux / macOS** — unzip the artifact and run the bundled
executable. macOS builds are unsigned; you may need to right-click → Open
the first time, or clear the quarantine flag:
```bash
xattr -cr /path/to/App.app
```

**Android** — unzip to get the `.apk`, then install it on a device or
emulator with `adb install app.apk` (enable "Install unknown apps" for
your file manager or ADB source first).

**iOS** — the `.ipa` requires a provisioning profile matching your device
to install outside the App Store (e.g. via Xcode or a tool like
AltStore/Sideloadly). The **iOS Simulator** build can be dragged directly
onto a running simulator, or installed with:
```bash
xcrun simctl install booted /path/to/App.app
```

**Web** — unzip and serve the folder with any static file server, e.g.:
```bash
python -m http.server --directory build/web 8000
```

## Reporting issues

Found a platform-specific bug in one of these builds? Please file it
against the control itself, with the platform and artifact link included:

[github.com/zaim-tech/flet-webview-all/issues](https://github.com/zaim-tech/flet-webview-all/issues)
