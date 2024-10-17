<script setup>
const props = defineProps(['title', 'buttonType', 'to'])
</script>

<template>
    <RouterLink v-if="props.buttonType === 'rounded'"
        class="inline-block rounded border border-indigo-600 bg-indigo-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-indigo-600 focus:outline-none focus:ring active:text-indigo-500"
        :to="props.to">
        {{ props.title }}
    </RouterLink>
    <RouterLink v-else class="group relative inline-block text-sm font-medium text-white focus:outline-none focus:ring"
        :to="props.to">
        <span class="absolute inset-0 border border-blue-600 group-active:border-blue-500"></span>
        <span
            class="block border border-blue-600 bg-blue-600 px-12 py-3 transition-transform active:border-blue-500 active:bg-blue-500 group-hover:-translate-x-1 group-hover:-translate-y-1">
            {{ props.title }}
        </span>
    </RouterLink>
</template>