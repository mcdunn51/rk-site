import React from 'react'
import Index from '../Components/Product'

const Product = (props) => {
    return (
        <Index id={props.match.params.id} />
    )
}

export default Product;