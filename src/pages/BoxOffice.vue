<template>
  <div class="container my-8">
  <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-8">
    <div  v-for="(item, index) in items" :key="index" class="bg-blue-100 rounded-md flex flex-col gap-2 justify-center px-5 py-4">


      <!-- <img :src="`https://imdb-api.com/API/ResizeImage?apiKey=k_lc0zmc7m&size=250x350&url=`+item.image" /> -->
      <img :src="item.image" />
      <h2 class="font-medium text-base md:text-sm text-gray-800 line-clamp-1 h-12" :title="item.title">

<router-link class="nav-link" to="/" >{{ item.title }}</router-link>
</h2>

<div class="">
                <div class="flex items-center ">
                  <svg
                    aria-hidden="true"
                    class="w-5 h-5 text-yellow-500"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <title>First star</title>
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    ></path>
                  </svg>
                  <span class="text-sm font-semibold"
                    >{{ item.rank }} / 10</span
                  >
                </div>
              </div>

    </div>
  </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "@vue/reactivity";
import axios from "axios";
const items: any = ref([]);
const loading = ref(true);
function get250List() {
  axios
    // .get('https://imdb-api.com/en/API/BoxOffice/k_lc0zmc7m')
    .get('https://raw.githubusercontent.com/mrmohsensami/api/main/boxoffice.json')
    .then(function (response) {
      items.value = response.data.items;
      loading.value = false;
    })
    .catch(function (error) {
      console.log(error);
    });
}
get250List();

</script>


<style scoped>
</style>