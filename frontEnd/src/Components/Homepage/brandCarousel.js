import React, { Component } from 'react';
import Slider from 'react-slick';

import akai from '../../images/brandCarousel/akai.png'
import carmen from '../../images/brandCarousel/carmen.png'
import cookincolour from '../../images/brandCarousel/cookincolour.png'
import elgento from '../../images/brandCarousel/elgento.png'
import itek from '../../images/brandCarousel/itek.png'
import morphyrichards from '../../images/brandCarousel/morphyrichards.png'
import nutrimaster from '../../images/brandCarousel/nutrimaster.png'
import pifco from '../../images/brandCarousel/pifco.png'
import teknique from '../../images/brandCarousel/teknique.png'
import tower from '../../images/brandCarousel/tower.png'
import warmlite from '../../images/brandCarousel/warmlite.png'
import warmnight from '../../images/brandCarousel/warmnight.png'


const BrandCarousel = () => {

    const settings = {
        infinite: true,
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: false,
        autoplaySpeed: 1000,
    }

    return (
        <div id="brandCarousel">
            <Slider {...settings}>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
                <div>
                    <img src="http://placekitten.com/g/300/100" />
                </div>
            </Slider>
        </div>
    )
}


export default BrandCarousel;


