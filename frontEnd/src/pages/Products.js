import React from 'react';
import Index from '../Components/Products/'

const Products = (props) => {
    return (
        <Index id={props.match.params.id} />
    )
}

export default Products;