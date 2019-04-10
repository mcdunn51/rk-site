import React from 'react';
import Slider from 'react-slick';
import {Container} from 'react-bootstrap';

import akai from '../../images/brandCarousel/akai.jpg'
import carmen from '../../images/brandCarousel/carmen.jpg'
import cookincolour from '../../images/brandCarousel/cookincolour.png'
import elgento from '../../images/brandCarousel/elgento.jpg'
import itek from '../../images/brandCarousel/itek.jpg'
import morphyrichards from '../../images/brandCarousel/morphyrichards.png'
import nutrimaster from '../../images/brandCarousel/nutrimaster.png'
import pifco from '../../images/brandCarousel/pifco.png'
import teknique from '../../images/brandCarousel/teknique.png'
import tower from '../../images/brandCarousel/tower.png'
import warmlite from '../../images/brandCarousel/warmlite.png'
import warmnight from '../../images/brandCarousel/warmnight.png'


const BrandCarousel = () => {

    const settings = {
        arrows: false,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: false,
        autoplaySpeed: 2000,
        centerMode: true,

    }

    return (
        <Container id="brandCarousel">
            <Slider {...settings}>
                {/* <div>
                    <img src={akai} />
                </div>
                <div>
                    <img src={carmen} />
                </div>
                <div>
                    <img src={elgento} />
                </div>
                <div>
                <img src={itek} />
                </div> */}
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
        </Container>
    )
}


export default BrandCarousel;


