import React, { Component } from 'react';
import { Container, Card, Form, Button } from 'react-bootstrap';
import axios from 'axios';
// import LogInForm from '../Components/login/loginForm'


const getLogInToken = (e) => {
    e.preventDefault();
    axios({
        method: 'post',
        url: 'http://100.1.253.16:8000/o/token/?grant_type=password&username=Mike&password=tas}Ng2uQ7?!rSS9&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M',
    })
        .then(res => {
            console.log(res.data);
            // send values with token
            const values = getLoginFormValues();
            console.log(values);
        })
}

const getLoginFormValues = () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
}

const loginPage = (getLogInToken) => {

    return (
        <Container>
            <Card>
                <Card.Body>
                    <Card.Title>Login</Card.Title>
                    <Form onSubmit={getLogInToken()}>
                        <Form.Group controlId="formBasicEmail">
                            <Form.Label>Username</Form.Label>
                            <Form.Control id="username" type="text" placeholder="Enter Username" required />
                        </Form.Group>
                        <Form.Group controlId="formBasicPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control id="password" type="password" placeholder="Password" required />
                        </Form.Group>
                        <Form.Group controlId="formBasicChecbox">
                            <Form.Check type="checkbox" label="Check me out" />
                        </Form.Group>
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                    </Form>

                </Card.Body>
            </Card>
        </Container>
    )
}


export default loginPage 