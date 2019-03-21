const addToCart = (cart, item) => {
    // get current cart
    console.log(cart)
    console.log(item)
    // add new item
    
}

const cartReducer = (state=[], action) => {
    switch(action.type) {
        case 'ADD_TO_CART':
            return addToCart(state, action.payload)
        
        default:
            return state
    }
}

export default cartReducer;