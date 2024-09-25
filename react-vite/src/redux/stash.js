const CREATE = 'stash/create';
const GET_USER_STASHES = 'user/stashes'
const GET_STASH_BY_ID = 'stashes/id'

//action return
const createStash = (stash) => {
    return {
        type: CREATE,
        payload: stash
    }
}

 const userStashes = (stashes) => {
    return {
        type:GET_USER_STASHES,
        payload: stashes
    }
 }
 
 const stashById = (stash) => {
    return {
        type: GET_STASH_BY_ID,
        payload: stash
    }
 }

//thunk create a stash
export const createStashThunk = (stash) => async dispatch => {
    const res = await fetch(`/api/stashes`, {
            method: "POST",
            body: stash
        });

    if(res.ok) {
        const data = await res.json()
        dispatch(createStash(data))
        return data
    } else {
        const err = await res.json()
        return err
    }
}

export const getUserStashes = (id) => async (dispatch) => {
    const res = await fetch(`/api/users/${id}/stashes`)
    const data = res.json();
    dispatch(userStashes(data))
}

export const getStashById = (id) => async (dispatch) =>{
    const res = await fetch(`/api/stashes/${id}`)
    const data = res.json()
    dispatch(stashById(data))
    
}

const initialState = { stash: null }


function stashReducer(state = initialState, action) {
    switch (action.type) {
        case CREATE:
            return {...state, stash: action.payload};
        case GET_USER_STASHES:
            return action.payload
        case GET_STASH_BY_ID:
            return action.payload
        default:
            return state
    }
}

export default stashReducer;
