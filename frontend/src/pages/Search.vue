<template>
<div class="h-[700px] container my-8">
    <div class="text-xl mb-4">
        <h1><span>search for: </span> {{ items.expression }}</h1>
    </div>
    <div
      class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-8"
    >
      <div
        v-for="(item, index) in items.results"
        :key="index"
        class="bg-blue-50 border border-blue-100 rounded-md flex flex-col gap-2 justify-center px-5 py-4"
      >
        <img :src="`https://imdb-api.com/API/ResizeImage?apiKey=k_lc0zmc7m&size=250x350&url=`+item.image" />
        <h2
          class="font-medium text-base md:text-sm text-gray-800 line-clamp-1"
          :title="item.title"
        >
          <router-link class="nav-link" :to="{name: 'single', params: { id: item.id } }">{{ item.title }}</router-link>
        </h2>

        <div class="">
          <div class="flex justify-between items-center">
            <span class="text-sm font-semibold">{{ item.description }}</span>
          </div>
        </div>
      </div>
    </div>
  </div> 
</template>
    
<script setup lang="ts">
import { ref } from "@vue/reactivity";
import axios from "axios";
import { useRoute } from "vue-router";
const items:any = ref([]);
const route = useRoute();
axios
    .get(
        `https://imdb-api.com/en/API/SearchMovie/k_g6l7enfv/${route.params.exp}`
    )
    .then(function (response) {
        items.value = response.data;
    })
    .catch(function (error) {
        console.log(error);
    });
</script>

<style scoped>
  nav {
    position: absolute;
    width: 100%;
    top: 0;
  }
</style>