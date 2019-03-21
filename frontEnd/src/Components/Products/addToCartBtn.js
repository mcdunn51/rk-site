import React from 'react';
import {Button} from 'react-bootstrap';

const AddToCartBtn = (props) => {
    return (
        <Button onClick={() => props.addToCart(props.product)}>Add to cart</Button>
    )
}

export default AddToCartBtn;
