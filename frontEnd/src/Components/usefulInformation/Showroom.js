import React from 'react'
import { Row, Col, Card } from 'react-bootstrap'

import showroomChina from '../../images/showRooms/showroomsChina.png'
import showroomUK from '../../images/showRooms/showroomsUK.png'

const ShowRoom = () => {
    return (
        <Col md={10} id="showRooms">
            <Row>
                <Col>
                    <p id="firstParagraph">
                        Designed to provide you the very best buying experience, our showrooms boasts 8000 sq/ft of products from
                        over 25 brands and spanning electrical, housewares, SDA and consumer electronics.
                    </p>
                    <p>
                        A perfectly replicated retail environment, our department store-like showrooms allow buyers to experience first-hand the merchandising opportunities our product ranges offer and to get up close and personal with the products themselves.
                    </p>
                    <p>
                        Our fully trained representatives are always on hand to answer any questions about product lines, ordering, fulfillment, shipping and merchandising, and will ensure that the time spent with us is hospitable and productive.
                    </p>
                </Col>
            </Row>
            <Row>
                <Col xs={12} md={6} className="mb-3">
                    <Card>
                        <Card.Title>UK</Card.Title>
                        <Card.Img variant="top" src={showroomUK} />
                        <Card.Body>
                            <ul>
                                <li>RKW Ltd</li>
                                <li>Sutton House</li>
                                <li>Berry Hill Road,</li>
                                <li>Stoke-on-Trent</li>
                                <li>ST4 2NL</li>
                                <li><strong>Tel:</strong> 0333 220 6070</li>
                            </ul>
                            <iframe className="map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2001.088811157678!2d-2.164373712688766!3d53.01286206781373!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x487a69ce535be327%3A0xd5bdfa1998cc3743!2sR+K+w+Ltd!5e0!3m2!1sen!2suk!4v1443707402914">
                            </iframe>
                        </Card.Body>
                    </Card>
                </Col>
                <Col xs={12} md={6} className="mb-3">
                    <Card>
                        <Card.Title>China</Card.Title>
                        <Card.Img variant="top" src={showroomChina} />
                        <Card.Body>
                            <ul>
                                <li>Guangzhou RKW Trading Company Limited</li>
                                <li>Room 308-311, No 512, Tower 2,</li>
                                <li>Guangzhou North Avenue,</li>
                                <li>Tianhe District, Guangzhou,</li>
                                <li>Guangdong, China</li>
                                <li><strong>Post code:</strong>510515</li>
                                <li><strong>Tel:</strong>+86 (0) 20 8526 9725 / +86 (0) 20 8526 9512</li>
                            </ul>
                            <iframe className="map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d917.0638488638108!2d113.31850382924377!3d23.160876999055226!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjPCsDA5JzM5LjIiTiAxMTPCsDE5JzA4LjYiRQ!5e0!3m2!1sen!2suk!4v1453304655916">
                            </iframe>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Col>
    )
}

export default ShowRoom;