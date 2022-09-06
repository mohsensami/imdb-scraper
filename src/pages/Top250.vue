<template>
  <div class="container my-8">
    <div
      class="flex justify-center items-center h-96"
      v-if="loading"
      role="status"
    >
      <svg
        aria-hidden="true"
        class="mr-2 w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
        viewBox="0 0 100 101"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
          fill="currentColor"
        />
        <path
          d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
          fill="currentFill"
        />
      </svg>
      <span class="sr-only">Loading...</span>
    </div>
  <div v-else class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-8">
    <div  v-for="(item, index) in items" :key="index" class="bg-blue-50 border border-blue-100 rounded-md flex flex-col gap-2 justify-center px-5 py-4">


      <!-- <img :src="`https://imdb-api.com/API/ResizeImage?apiKey=k_lc0zmc7m&size=250x350&url=`+item.image" /> -->
      <img :src="item.image" />
      <h2 class="font-medium text-base md:text-sm text-gray-800 line-clamp-1" :title="item.title">

<router-link class="nav-link" :to="{name: 'single', params: { id: item.id } }" >{{ item.title }}</router-link>
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
                    >{{ item.imDbRating }} / 10</span
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
    .get('https://raw.githubusercontent.com/mrmohsensami/api/main/top250.json')
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