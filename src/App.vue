<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import ControlBar from './components/ControlBar.vue'
import Viewer from './components/Viewer.vue';
const route = useRoute()

const data_url = 'http://www.s1023143047.onlinehome.us/'

var datasets = ref([])
var active_dataset = ref(null)
var hidden_overlays = ref({})

watch(() => route.params.dataset, (newRoute, oldRoute) => {
  hidden_overlays.value = {}
  for (const [key, value] of Object.entries(route.query)) {
    if (value == 'hide') {
      hidden_overlays.value[key] = true
    }
  }
  if (newRoute.params.area == oldRoute.params.area && datasets.value.length > 0) {
    return
  }
  if (newRoute.params.dataset != undefined) {
    console.log("Loading data")
    fetch(data_url + newRoute.params.dataset + '/' + newRoute.params.dataset + '.json')
      .then(response => response.json())
      .then(data => {

        datasets.value = data["datasets"].reduce((acc, entry) => {
          acc[entry.name] = entry;
          return acc;
        }, {})
        if (route.params.area != undefined) {
          if (route.params.area != active_dataset.value) {
            console.log("Changing area")
            active_dataset.value = route.params.area
          }
        } else {
          active_dataset.value = Object.keys(datasets.value)[0]
        }
        
      })
  }
})
</script>
<template>
  <Viewer :dataset="datasets[active_dataset]" :hidden_overlays="hidden_overlays" />
  <ControlBar :hidden_overlays="hidden_overlays" :datasets="datasets" :active_dataset="active_dataset" />

</template>
