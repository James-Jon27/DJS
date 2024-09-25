const CREATE = 'stash/create';
const GET_USER_STASHES = 'user/stashes'
const GET_STASH_BY_ID = 'stashes/id'
const UPDATE_STASH = 'stashes/id/update'
const DELETE_STASH = 'stashes/id/delete'

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

 const updateStash = (stash) => {
    return {
        type: UPDATE_STASH,
        payload: stash
    }
 }

 const deleteStash = (id) => {
    return {
        type: DELETE_STASH,
        payload: id
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
    const data = await res.json();
    dispatch(userStashes(data))
}

export const getStashById = (id) => async (dispatch) =>{
    const res = await fetch(`/api/stashes/${id}`)
    const data = await res.json()
    dispatch(stashById(data))
}

export const updateStashById = (id, update) => async (dispatch) => {
    const res = await fetch(`/api/stashes/${id}`, {
        method: "POST",
        body: update
    })

    const data = await res.json()
    dispatch(updateStash(data))


}

export const deleteStashById = (id) => async (dispatch) => {
    await fetch(`/api/stashes/${id}`, {
        method: "DELETE"
    })

    dispatch(deleteStash(id))
}

const initialState = { stash: null }

function stashReducer(state = initialState, action) {
    switch (action.type) {
        case CREATE:
            return {...state, [action.payload.id]:action.payload};
        case GET_USER_STASHES:
            return action.payload
        case GET_STASH_BY_ID:
            return action.payload
        case UPDATE_STASH:
            return {...state, [action.payload.id]:action.payload}
        case DELETE_STASH:{
            const newState = {...state}
            delete newState[action.payload]
            return newState
        }
        default:
            return state
    }
}

export default stashReducer;
