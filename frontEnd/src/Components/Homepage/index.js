import React from 'react';

import HomePageCarousel from './carousel';
import DeliveryStrapline from './deliveryStrapline';
import Over25years from './over25years';
import AboutUsPanel from './aboutUsPanel';
import BrandCarousel from './brandCarousel';
import NewsletterSignUpBar from './newsletterSignUpBar';


const Index = () => {
    return (
        <div>
            <DeliveryStrapline/>
            <HomePageCarousel/>
            <Over25years/>
            <AboutUsPanel/>
            <BrandCarousel/>
            <NewsletterSignUpBar/>
        </div>
    )
}
export default Index;