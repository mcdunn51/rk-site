import React, { Component } from 'react';
import { Container, Nav } from 'react-bootstrap';
import { IndexLinkContainer } from 'react-router-bootstrap';
import axios from 'axios';
import { connect } from 'react-redux';

class MainNavbar extends Component {

    // get all brand names
    // componentDidMount() {

    //     const { loadBrands } = this.props

    //     axios({
    //         method: 'get',
    //         url: `http://100.1.253.16:8000/Manufacturer/`,
    //         headers: { 'Authorization': 'Bearer SDhm0d95wxYxnBzeFIEXL2Fbev14GW' },
    //     })
    //         .then(res => {
    //             console.log(res.data)
    //             const manufacturerCodes = [];
    //             res.data.forEach(element => {
    //                 manufacturerCodes.push(element.manufacturerCode);
    //             })
    //             loadBrands(manufacturerCodes)
    //         })
    // };


    render() {
        

        return (
            <Container fluid={true} id="mainNavBar">
                <Container>
                    <Nav
                        activeKey="/home"
                        onSelect={selectedKey => alert(`selected ${selectedKey}`)}
                    >
                        <Nav.Item>
                            <Nav.Link>ELECTRICALS</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="link-1">HOUSEWARES</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="link-2">GARDEN & LEISURE</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="link-3">SHOP BY BRAND</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="link-4">BEST SELLERS</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link eventKey="link-5">CLEARANCE & SPECIALS</Nav.Link>
                        </Nav.Item>
                    </Nav>
                </Container>
            </Container>
        )
    }
}

// function mapStateToProps(state) {
//     return {
//         brands: state.brands
//     }
// }

// function mapDispatchToProps(dispatch) {
//     return {
//         loadBrands: (brands) => {
//             dispatch({ type: 'LOAD_BRANDS', payload: brands })
//         }
//     }
// }

export default MainNavbar;


