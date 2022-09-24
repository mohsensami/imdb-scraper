<template>
  {{ item }}
</template>

<script>
import { ref } from "@vue/reactivity";
import axios from "axios";
import { useRoute } from "vue-router";
const item = ref([]);
const loading = ref(true);
const route = useRoute();
export default {
    setup() {
    function getActor() {
      axios
        .get(
          `https://imdb-api.com/en/API/Awards/k_g6l7enfv/${route.params.id}`
        )
        .then(function (response) {
          item.value = response.data;
          loading.value = false;
        })
        .catch(function (error) {
          console.log(error);
        });
    }
    getActor();
    return {
        getActor,
        item,
        route
    }
    }
}
</script>

<style>

</style>