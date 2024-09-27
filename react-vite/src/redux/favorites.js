const GET_FAVES = "favorites/get";
const ADD_FAV = "user/add-favorite";
const DEL_FAV = "user/delete-favorite";

const getFavs = (favorites) => {
	return {
		type: GET_FAVES,
		payload: favorites,
	};
};

const addfav = (imageUpdate) => {
	return {
		type: ADD_FAV,
		payload: imageUpdate,
	};
};

const delFav = (favToDelete) => {
	return {
		type: DEL_FAV,
		payload: favToDelete,
	};
};

export const getFavoritesThunk = (id) => async (dispatch) => {
	const res = await fetch(`/api/users/${id}/favorites`);
	const data = await res.json();
	dispatch(getFavs(data));
};

export const addFavToUser = (id) => async (dispatch) => {
	const res = await fetch(`/api/images/${id}/favorite`, {
		method: "POST",
	});
	const data = await res.json();
	dispatch(addfav(data));
};

export const delFavFromUser = (id) => async (dispatch) => {
	const res = await fetch(`/api/favorites/${id}`, {
		method: "DELETE",
	});
	const data = await res.json();
	dispatch(delFav(data));
};


export default function favoriteReducer(state = {}, action) {
    switch(action.type) {
        case GET_FAVES: {
            return action.payload
        }
        case ADD_FAV: {
            return {...state, [action.payload.id]: action.payload}
        }
        case DEL_FAV: {
            const newState = {...state}
            delete newState[action.payload]
            return newState
        }
        default:
            return state
    }
}