<template>
<div class='h-[700px] flex-center flex-col gap-16'>
  <h1 class="text-5xl font-bold">FILM REVIEW · MOVIE DATABASE</h1>
  <div class="flex">
    <input v-on:keyup.enter="submitSearch()" v-model="search" class="border-2 border-gray-500 rounded-l focus:outline-0 w-96 h-10 px-2" type="text"> <button @click="submitSearch()" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-r">Search</button>
  </div>
</div>
</template>
  
<script setup lang="ts">
  import { useRouter } from "vue-router";
  import { ref } from "@vue/reactivity";
  const item:any = ref([]);
  const router = useRouter();
  let search = ref('')
  function submitSearch() {
    router.push({ name: 'Search', params: { exp: search.value } })
  } 
  </script>
  
<style scoped>
  nav {
    position: absolute;
    width: 100%;
  }
</style>