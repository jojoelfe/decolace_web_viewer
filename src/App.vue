<script setup>
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ControlBar from './components/ControlBar.vue'
import Viewer from './components/Viewer.vue';
const route = useRoute()
const router = useRouter()
const data_url = 'http://www.s1023143047.onlinehome.us/'

var datasets = ref([])
var active_dataset = ref(null)
var hidden_overlays = ref({})


watch(() => route.query, (newValue, oldValue) => {
  hidden_overlays.value = {}
  for (const [key, value] of Object.entries(newValue)) {
    if (value == 'hide') {
      hidden_overlays.value[key] = true
    }
  }
})

watch(() => route.params.area, (newValue, OldValue) => {
  if (newValue != undefined) {
    active_dataset.value = newValue
  }
})

watch(() => route.params.dataset, (newValue, OldValue) => {
  
  if (newValue != undefined) {
    fetch(data_url + newValue + '/' + newValue + '.json')
      .then(response => response.json())
      .then(data => {

        datasets.value = data["datasets"].reduce((acc, entry) => {
          acc[entry.name] = entry;
          return acc;
        }, {})
        if (route.params.area == undefined) {
          router.push({name: 'area', params: {area: Object.keys(datasets.value)[0]}})
        }
        
      })
  }
})
</script>
<template>
  <Viewer :dataset="datasets[active_dataset]" :hidden_overlays="hidden_overlays" />
  <ControlBar :hidden_overlays="hidden_overlays" :datasets="datasets" :active_dataset="active_dataset" />

</template>
