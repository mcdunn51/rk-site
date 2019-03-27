import React from 'react';

import HomePageCarousel from './carousel';
import DeliveryStrapline from './deliveryStrapline';
import Over25years from './over25years';
import AboutUsPanel from './aboutUsPanel';


const Index = () => {
    return (
        <div>
            <DeliveryStrapline/>
            <HomePageCarousel/>
            <Over25years/>
            <AboutUsPanel/>
        </div>
    )
}
export default Index;