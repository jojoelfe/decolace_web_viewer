<script setup>
import { ref, onMounted, watch } from 'vue'
import OpenSeadragon from 'openseadragon'
import { ossb } from '@/openseadragon-scalebar.js'

ossb(OpenSeadragon)

var viewer
var datasets = ref([])
var active_dataset = ref(null)
var match_overlays = ref([])

watch(match_overlays, () => {
  if (viewer == undefined) {
    return
  }
  for (var i = 0; i < match_overlays.value.length; i++) {
    var match_overlay = match_overlays.value[i]
    if (viewer.world.getItemAt(i+1) == undefined) {
      continue
    }
    //for (var j = 0; j < match_overlay.alternatives.length; j++) {
    //  if (match_overlay.alternatives[j].show) {
    //    
    //  }
    //}
    if (match_overlay.show) {
      if (match_overlay.alternatives[0].show) {
        viewer.world.getItemAt(i+1).setOpacity(0)
        viewer.world.getItemAt(i+2).setOpacity(1)
      } else {
        viewer.world.getItemAt(i+1).setOpacity(1)
        viewer.world.getItemAt(i+2).setOpacity(0)
      }
    } else {
      viewer.world.getItemAt(i+1).setOpacity(0)
      viewer.world.getItemAt(i+2).setOpacity(0)
    }
  }
}, {deep: true})

watch(active_dataset, () => {
  if (viewer == undefined) {
    return
  }
  var dataset = datasets.value[active_dataset.value]
  match_overlays.value = []
  viewer.open({
    tileSource: dataset["micrograph"]["default"],
    x: 0,
    y: 0,
  })
  for (var i = 0; i < dataset["match_overlays"].length; i++) {
        var match_overlay = dataset["match_overlays"][i]
        viewer.addTiledImage({
          tileSource: match_overlay["default"],
          x: 0,
          y: 0,
          opacity: 1,
          index: 1
        })
        viewer.addTiledImage({
          tileSource: match_overlay["alternatives"][0]["url"],
          x: 0,
          y: 0,
          opacity: 0,
          index: 2
        })
        match_overlay.show = true
        for (var j = 0; j < match_overlay["alternatives"].length; j++) {
          var alternative = match_overlay["alternatives"][j]
          alternative.show = false
        }
        match_overlays.value.push(match_overlay)
      }
  })

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
  // Fetch '/erhox_data.json' and add it to the viewer
  fetch('erhox_data.json')
    .then(response => response.json())
    .then(data => {
      datasets.value = data["datasets"]
      active_dataset.value = 0
      
    })
})
</script>

<template>
  <div id="openseadragon1">
    <div id="openseadragon1_controls">
      <h3>Control Overlays:</h3>
      <div v-for="match_overlay in match_overlays" :key="match_overlay.name">
        <input type="checkbox" id="showribosomes" v-model="match_overlay.show" />
        <label for="checkbox"> Show {{ match_overlay.name }}</label>
        <div v-for="alternative in match_overlay.alternatives" :key="alternative.name" class="alternative-overlay">
          <input type="checkbox" id="showribosomes" v-model="alternative.show" />
          <label for="checkbox"> {{ alternative.name }}</label>
        </div>
      </div>
      <h3>Datasets:</h3>
      <div id="dataset_list">
      <a v-for="(dataset, i) in datasets" :key="dataset.name" class="dataset" href="#" @click.prevent="active_dataset = i">
        <p>{{ dataset.name }}</p>
        <img :src="dataset.thumbnail" />
      </a>
      
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
  right: 0px;
  top:10px;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  height: 75vh;
  padding: 10px;
  background-color: rgba(0, 0, 0, 0.336);
  z-index: 9999;
  display: block;
  transition: transform .15s 0s !important;
}



#openseadragon1_controls:not(:hover) {
    transform: translateX(90%);
    transition: transform .8s 0s!important; /* Originally: 2s 1s */
	transition-delay: 2s !important;
}

#openseadragon1_controls img {
  width: 5vw;
  margin: auto auto;
  display: block;
}

#openseadragon1_controls #dataset_list {
  overflow: auto;
  height: 75%;
}

#openseadragon1_controls .dataset {
  display:block;
}

#openseadragon1_controls .alternative-overlay {
  margin-left: 20px;
}

#openseadragon1_controls p {
  color: var(--vt-c-white-soft);
  text-align: center;
}

#openseadragon1_controls label {
  color: var(--vt-c-white-soft);
}

#openseadragon1_controls h3 {
  color: var(--vt-c-white-soft);
  font-weight: 600;
}

.openseadragon-canvas:focus {
  outline: none;
}
</style>
