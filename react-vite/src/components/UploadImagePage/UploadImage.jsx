import {useState} from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { createImage } from "../../redux/image";


const UploadImage = () => {
    const navigate = useNavigate(); // so that you can redirect after the image upload is successful
    const dispatch = useDispatch();
    const [image, setImage] = useState(null);
    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    const [labels, setLabels] = useState('')
    const [imageLoading, setImageLoading] = useState(false);
    
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("image", image);
        formData.append("title", title)
        formData.append("description", description)
        const label_arr = labels.replaceAll(' ', '').split(',')
        formData.append("labels", label_arr)
        
        // aws uploads can be a bit slow—displaying
        // some sort of loading message is a good idea
        setImageLoading(true);
        await dispatch(createImage(formData));
        navigate("/");
    }
     
    return (
        <form 
            onSubmit={handleSubmit}
            encType="multipart/form-data"
        >
            <label>
                Title
                <input 
                 type="text"
                 value={title}
                 onChange={(e) => setTitle(e.target.value)}
                 required
                />
            </label>
            <label>
                Description
                <input 
                 type="text"
                 value={description}
                 onChange={(e) => setDescription(e.target.value)}
                 required 
                />
            </label>
            <label>
                Labels
                <input 
                 type="text"
                 value={labels}
                 onChange={(e) => setLabels(e.target.value)}
                />
            </label>
            <input
              type="file"
              accept="image/*"
              onChange={(e) => setImage(e.target.files[0])}
            />
            <button type="submit">Submit</button>
            {(imageLoading)&& <p>Loading...</p>}
        </form>
    )
}

export default UploadImage;