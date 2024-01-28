# decolace_web_viewer

A web-based  viewer for [DeCo-LACE](https://github.com/jojoelfe/decolace) data.

[Click here](https://jojoelfe.github.io/decolace_web_viewer) for an example dataset

## Description of pipeline

- Images are rendered in blender at high resolution (~25kx25k). The montaged micrograph is imported as a tiff texture and molecules are imported using [Molecular Nodes](https://github.com/BradyAJohnston/MolecularNodes).

    - Every dataset is one scene in the blenderfile. The micrograph and molecular overlay layers are ViewLayers within the scene. The compositor is used to save them all into seperate files.
    - There is a custom renderscript that uses renderregions to break the rendered image up into 4 quadrants. Otherwise the compositor crashes even on machines with a lot of RAM (512GB).
    - The orthographic scale of the camera is driven by a driver based on the render resolution. That ensures a constant pixel-size.
    - The rendered quadrants are placed into a folder called "output"
    - An example .blend file with the nescessary data can be downloaded [here](https://hidrive.ionos.com/lnk/AeGglN01)

- The script [assemble_dzi.py](preprocessing_scripts/assemble_dzi.py) is used to assemble the quadrants and then write out image pyramids in dzi format.
- The script [optimize_png.sh](preprocessing_scripts/optimize_png.sh) is used to optimize the filesize of the dzi image pyramid (from ~1GB to 250MB)
- The resuting dzi files are uploaded to a static hosting service.
- The webapp in this repo can read specifications in json format to display the dzi files. [Example](public/erhox_data.json)

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
pnpm install
```

### Compile and Hot-Reload for Development

```sh
pnpm dev
```

### Compile and Minify for Production 

```sh
pnpm build
```

### Lint with [ESLint](https://eslint.org/)

```sh
pnpm lint
```
