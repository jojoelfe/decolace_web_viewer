<script setup>
import { onMounted, watch } from 'vue'
import OpenSeadragon from 'openseadragon'
import { ossb } from '@/openseadragon-scalebar.js'

ossb(OpenSeadragon)

var viewer
const props = defineProps(['dataset', 'hidden_overlays'])


async function update_overlays() {
    if (viewer == undefined) {
    return
  }
  if (props.dataset == undefined) {
    return
  }

  for (var i = 0; i < props.dataset.match_overlays.length; i++) {
    var match_overlay = props.dataset.match_overlays[i]
    if (viewer.world.getItemAt(i+1) == undefined) {
      console.log("skipping")
      continue
    }
    if (match_overlay.name in props.hidden_overlays) {
      console.log("setting opacity to 0")
      viewer.world.getItemAt(i+1).setOpacity(0)
    } else {
      console.log("setting opacity to 1")
      viewer.world.getItemAt(i+1).setOpacity(1)
    }
  }
}

watch(() => props.hidden_overlays, update_overlays, {deep: true})

function update_dataset() {
  console.log("updating dataset")
  if (viewer == undefined) {
    return
  }
  if (props.dataset == undefined) {
    return
  }
  viewer.open({
    tileSource: {
      'type': 'image',
      'url': props.dataset["micrograph"]["default"]
    },
    x: 0,
    y: 0,
  })
  for (var i = 0; i < props.dataset["match_overlays"].length; i++) {
        var match_overlay = props.dataset["match_overlays"][i]
        viewer.addTiledImage({
          tileSource: {
            'url': match_overlay["default"],
            'type': 'image'
          },
          x: 0,
          y: 0,
          opacity: 1,
          index: 1
        })
        
      }

}

watch(() => props.dataset,update_dataset)

onMounted(() => {
  viewer = OpenSeadragon({
    id: 'openseadragon1',
    subPixelRoundingForTransparency: OpenSeadragon.SUBPIXEL_ROUNDING_OCCURRENCES.ONLY_AT_REST,
    showNavigator: true,
    navigatorPosition:   "BOTTOM_RIGHT",
    prefixUrl: 'https://openseadragon.github.io/openseadragon/images/',
    tileSources: [
      
    ]
  })
  viewer.scalebar({
    minWidth: '75px',
    pixelsPerMeter: 666666666.667,
    color: 'rgb(150, 150, 150)',
    fontColor: 'rgb(50, 50, 50)',
    backgroundColor: 'rgba(255, 255, 255, 0.5)'
  })
})


</script>

<template>
  <div id="openseadragon1">
  </div>
</template>

<style scoped>
#openseadragon1 {
  width: 100vw;
  height: 100vh;
  margin: auto auto;
}

.openseadragon-canvas:focus {
  outline: none;
}
</style>
