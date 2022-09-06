<template>
<div class=''>

</div>
</template>
  
<script setup lang="ts">
  import { useRoute, useRouter } from "vue-router";
  import { ref } from "@vue/reactivity";
  const item:any = ref([]);
  const route = useRoute();
  const router = useRouter();
  let search = ref('')
  function submitSearch() {
  router.push({ name: 'Search', params: { exp: search.value } })
  } 
  </script>
  
  <style>
  
  </style>