import React from 'react';
import { Row, Col } from 'react-bootstrap';

const AboutUs = () => {
    return (
        <Col md={10} id="aboutUs">
            <Row>
                <Col>
                    <p id="firstParagraph">
                        Celebrating over 25 Years in Business, RKW is Europes leading electricals and housewares distributor and boasts an impressive
                        portfolio of high-profle brands.
                    </p>
                </Col>
            </Row>

            <Row>
                <Col xl={9}>
                    <p>
                        Proud to boast, RKW own several major brands, including Tower, Carmen, Signature, Teknique, Itek and Warmlite/Warmnite, and
                        also licenses the Morphy Richards brand for cookware and housewares as well as the Akai and Pifco brands. In addition, RKW also
                        stocks and distributes leading brands including Tefal, Russell Hobbs, Vax and Panasonic.
                    </p>
                    <h4>
                        What we Offer
                    </h4>
                    <p>
                        Operating from our global distribution and drop-ship fulfilment centre in Staffordshire, we have 345,000sq ft stocked with over
                        3,500 product lines to ensure next-day delivery anywhere in the UK.
                    </p>
                    <p>
                        Covering product categories spanning cookware, housewares, heating, and perhaps the widest selection of SDAs in the industry,
                        we offer a comprehensive solution to trade clients. With offices in the UK and Mainland China, we are perfectly placed to order
                        trading partners top quality brands and deals exclusive to specific markets.
                    </p>
                    <p>
                        Our highly trained buying, product development, marketing and IT integration teams have years of industry knowledge and
                        experience and are incredibly adept at using brand placement and channel control to offer exclusive product, brands and
                        packaging.
                    </p>
                    <p>
                        Full product ranges from all of our brands, both proprietary and licensed, can be viewed at our expansive showroom in the heart of
                        the Midlands or via the relevant brand sections of this website.
                    </p>
                </Col>
                <Col md={3} id="aboutUsImgCol" className="d-none d-xl-block pl-0">
                    <img src="http://placekitten.com/222/333" />
                </Col>

            </Row>
        </Col>
    )
}

export default AboutUs;