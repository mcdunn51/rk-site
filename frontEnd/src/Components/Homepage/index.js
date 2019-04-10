import React from 'react';

import HomePageCarousel from './carousel';
import Over25years from './over25years';
import AboutUsPanel from './aboutUsPanel';
import BrandCarousel from './brandCarousel';



const Index = () => {
    return (
        <div>
            <HomePageCarousel/>
            <Over25years/>
            <AboutUsPanel/>
            <BrandCarousel/>
        </div>
    )
}
export default Index;