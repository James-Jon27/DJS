const GET_USER_FAVORITES = 'user/favorites'

const userFav = (favs) => {
    return {
        type: GET_USER_FAVORITES,
        payload: favs
    }
}

export const getUserFavorites = (id) => async (dispatch) => {
    const res = await fetch(`/users/${id}/favorites`)
    const data = await res.json()
    dispatch(userFav(data))
}


function favoriteReducer(state = {}, action){
    switch(action.type){
        case GET_USER_FAVORITES:
            return {...state, ...action.payload}
        default:
            return state
    }
}

export default favoriteReducer