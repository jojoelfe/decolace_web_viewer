<script setup>
import { ref, watch } from 'vue'
import { RouterLink, useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const potential_overlays = ref([])

const props = defineProps(['hidden_overlays', 'datasets', 'active_dataset'])
watch(() => props.datasets, (newVal, oldVal) => {
  potential_overlays.value = []
  for (const dataset of Object.values(newVal)) {
    for (const overlay of dataset.match_overlays) {
      if (!potential_overlays.value.includes(overlay.name)) {
        potential_overlays.value.push(overlay.name)
      }
    }
  }
})
</script>

<template>
 <div id="openseadragon1_controls">
      <h3>Overlays:</h3>
      <div v-for="overlay in potential_overlays" :key="overlay">
        <input type="checkbox" id="showribosomes" :checked="!(overlay in hidden_overlays)" @change="query = router.query;nq = {};nq[overlay] = $event.target.checked ? 'show' : 'hide';router.push({query: {...$event.query,...nq}});"/>
        <label for="checkbox"> Show {{ overlay }}</label>
        
      </div>
      <h3>Datasets:</h3>
      <div id="dataset_list">
      <RouterLink v-for="[area, dataset] in Object.entries(props.datasets)" :key="area" class="dataset" :to="{ name: 'area', params: {'area': area} }">
        <p :class="{'active': area==active_dataset}">{{ dataset.name }}</p>
        <img :src="dataset.thumbnail" />
      </RouterLink>
      
    </div>
    </div>
</template>

<style scoped>


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

#openseadragon1_controls p.active {
  color: olivedrab;
}

#openseadragon1_controls label {
  color: var(--vt-c-white-soft);
}

#openseadragon1_controls h3 {
  color: var(--vt-c-white-soft);
  font-weight: 600;
}
</style>