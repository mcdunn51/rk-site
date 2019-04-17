import React from 'react';
import Slider from 'react-slick';
import { Container } from 'react-bootstrap';

import akai from '../../images/brandCarousel/akai.png'
import blackDecker from '../../images/brandCarousel/blackDecker.png'
import carmen from '../../images/brandCarousel/carmen.png'
import elgento from '../../images/brandCarousel/elgento.png'
import itek from '../../images/brandCarousel/itek.png'
import morphyrichards from '../../images/brandCarousel/morphyRichards.png'
import pifco from '../../images/brandCarousel/pifco.png'
import russellHobbs from '../../images/brandCarousel/russellHobbs.png'
import signature from '../../images/brandCarousel/signature.png'
import tower from '../../images/brandCarousel/tower.png'
import warmlite from '../../images/brandCarousel/warmlite.png'
import warmnite from '../../images/brandCarousel/warmnite.png'
// import cookincolour from '../../images/brandCarousel/cookincolour.png'
// import nutrimaster from '../../images/brandCarousel/nutrimaster.png'
// import teknique from '../../images/brandCarousel/teknique.png'




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
                <div>
                    <img src={akai} />
                </div>
                <div>
                    <img src={blackDecker} />
                </div>
                <div>
                    <img src={carmen} />
                </div>
                <div>
                    <img src={elgento} />
                </div>
                <div>
                    <img src={itek} />
                </div>
                <div>
                    <img src={morphyrichards} />
                </div>
                <div>
                    <img src={pifco} />
                </div>
                <div>
                    <img src={russellHobbs} />
                </div>
                <div>
                    <img src={signature} />
                </div>
                <div>
                    <img src={tower} />
                </div>
                <div>
                    <img src={warmlite} />
                </div>
                <div>
                    <img src={warmnite} />
                </div>
            </Slider>
        </Container>
    )
}


export default BrandCarousel;


