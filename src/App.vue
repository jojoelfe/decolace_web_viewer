<script setup>
import { ref, onMounted, watch } from 'vue'
import OpenSeadragon from 'openseadragon'
import { ossb } from '@/openseadragon-scalebar.js'

ossb(OpenSeadragon)

var viewer
var ribosomes = ref(true)
var dc_ribosomes = ref(false)

function set_ribosomes(show, dc) {
  if (show) {
    if (dc) {
      viewer.world.getItemAt(1).setOpacity(0)
      viewer.world.getItemAt(2).setOpacity(1)
    } else {
      viewer.world.getItemAt(1).setOpacity(1)
      viewer.world.getItemAt(2).setOpacity(0)
    }
    
  } else {
    viewer.world.getItemAt(1).setOpacity(0)
    viewer.world.getItemAt(2).setOpacity(0)
  }
}

watch(ribosomes, (value) => {
  set_ribosomes(value, dc_ribosomes.value)
})

watch(dc_ribosomes, (value) => {
  set_ribosomes(ribosomes.value, value)
})

onMounted(() => {
  viewer = OpenSeadragon({
    id: 'openseadragon1',
    subPixelRoundingForTransparency: OpenSeadragon.SUBPIXEL_ROUNDING_OCCURRENCES.ONLY_AT_REST,
    showNavigator: true,
    navigatorPosition:   "BOTTOM_RIGHT",
    prefixUrl: 'https://openseadragon.github.io/openseadragon/images/',
    tileSources: [
      {
        tileSource: 'https://static.elferich.me/dzi/EUC_Lamella1/micrograph.dzi',
        x: 0,
        y: 0
      },
      {
        tileSource: 'https://static.elferich.me/dzi/EUC_Lamella1/ribosomes.dzi',
        x: 0,
        y: 0
      },
      {
        tileSource: 'https://static.elferich.me/dzi/EUC_Lamella1/ribosomes_dc.dzi',
        x: 0,
        y: 0,
        opacity: 0
      }
    ]
  })
  viewer.scalebar({
    minWidth: '75px',
    pixelsPerMeter: 666666666.667,
    color: 'rgb(150, 150, 150)',
    fontColor: 'rgb(50, 50, 50)',
    backgroundColor: 'rgba(255, 255, 255, 0.5)'
  })
  document.getElementById('ribosomeCheckbox').checked = true
})
</script>

<template>
  <div id="openseadragon1">
    <div id="openseadragon1_controls">
      <div>
        <input type="checkbox" id="showribosomes" v-model="ribosomes" />
        <label for="checkbox">Show ribosomes</label>
      </div>
      <div>
        <input type="checkbox" id="showribosomes" v-model="dc_ribosomes" />
        <label for="checkbox">Depth cue</label>
      </div>
    </div>
  </div>
</template>

<style scoped>
#openseadragon1 {
  width: 100vw;
  height: 100vh;
  margin: auto auto;
}

#openseadragon1_controls {
  position: absolute;
  right: 60px;
  padding: 10px;
  background-color: rgba(255, 255, 255, 0.5);
  z-index: 9999;
  display: block;
}

.openseadragon-canvas:focus {
  outline: none;
}
</style>
