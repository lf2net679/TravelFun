<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';

import { mockHotCitys, mockNews } from './_Context';
import HotCity from './components/HotCity.vue';
import Member from './components/Member.vue';
import Search from './components/Search.vue';
import { useProductStore } from '@/stores';
import { SwiperNews, SwiperProduct } from '@/components/Swiper';
import Banner from '@/components/Banner.vue';
import AiChat from '@/components/AiChat/AiChat.vue';
import Footer from '@/components/Footer.vue';

const router = useRouter();

const productStore = useProductStore();

const { getByNewest, getByPopular } = storeToRefs(productStore);

const { getFilterData } = productStore;

const goCountry = () => router.push({ name: 'Country', params: { countryName: 'taiwan' } });
</script>

<template>
  <main>
    <Banner bg-url="/images/banner.jpg" :center="false">
      <template #title>
        <span>旅遊趣</span>
        陪你去台灣各地
      </template>
      <template #sec-title>
        讓我們帶著你一同欣賞台灣的美
      </template>
      <Search />
    </Banner>
    <div class="mb-4 md:mt-[60px] md:mb-0">
      <SwiperNews :news="mockNews" />
    </div>
    <img src="/images/travel-the-world.png" alt="travel world fun" class="-z-10 hidden -translate-y-8 md:block">
    <SwiperProduct title="Top 10 商品" sec-title="尋找最受歡迎的商品嗎？別再猶豫，立刻挑選！" :products="getFilterData(getByPopular)" />
    <img src="/images/home-bg.png" alt="home bg" class="my-6" loading="lazy">
    <SwiperProduct
      title="最新產品" sec-title="一直關注最新產品的我們，給您帶來最好的選擇和品質！" :btn="{ text: '查看更多' }"
      :products="getFilterData(getByNewest)" @btn-click="goCountry"
    />
    <HotCity :hot-citys="mockHotCitys" />
    <Member />
    <AiChat />
  </main>
  <Footer />
</template>
