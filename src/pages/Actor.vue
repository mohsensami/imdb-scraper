<template>
  <div class="container">
    <div class="grid grid-cols-12 gap-4">
        <div class="col-span-4">
            <img :src="item.image" :alt="item.name">
        </div>
        <div class="col-span-8">
            <h1 class="text-2xl">{{ item.name }}</h1>
            <small class="text-gray-500">{{ item.role }}</small>
            <p>{{ item.summary }}</p>
            <p>{{ item.birthDate }}</p>
            <p>{{ item.awards }}</p>
            <p>{{ item.height }}</p>
        </div>
    </div>
    <div>
        <ul class="md:flex justify-between gap-8">
            <li v-for="(known, index) in item.knownFor" :key="index">
                {{ known.title }}
                <img :src="`https://imdb-api.com/API/ResizeImage?apiKey=k_g6l7enfv&size=250x400&url=`+known.image" :alt="known.title">
            </li>
        </ul>
    </div>



<div class="flex flex-col">
  <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
    <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
      <div class="overflow-hidden">
        <table class="min-w-full">
          <thead class="bg-white border-b">
            <tr>
              <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                #
              </th>
              <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                Title
              </th>
              <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                Role
              </th>
              <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                Year
              </th>
              <th scope="col" class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                Description
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(cast, index) in item.castMovies" :key="index" class="bg-gray-100 border-b">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ index }}</td>
              <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                {{ cast.title }}
              </td>
              <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                {{ cast.role }}
              </td>
              <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                {{ cast.year }}
              </td>
              <td class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                {{ cast.description }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>


  </div>
</template>

<script setup lang="ts">
    import { Icon } from '@iconify/vue';
    import { ref } from "@vue/reactivity";
    import axios from "axios";
    import { useRoute } from "vue-router";
    const item:any = ref([]);
    const loading = ref(true);
    const route = useRoute();
    
    function getActor() {
      axios
        .get(
          `https://imdb-api.com/en/API/Name/k_g6l7enfv/${route.params.id}`
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
    
</script>

<style>

</style>