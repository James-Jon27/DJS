import { useModal } from "../../context/Modal";

function OpenModalImageItem({
	modalComponent, // component to render inside the modal
	src, // source of image
    alt, //desc/title of image or "Image"
	onItemClick, // optional: callback function that will be called once the button that opens the modal is clicked
	onModalClose, // optional: callback function that will be called once the modal is closed
}) {
	const { setModalContent, setOnModalClose } = useModal();

	const onClick = () => {
		if (onModalClose) setOnModalClose(onModalClose);
		setModalContent(modalComponent);
		if (typeof onItemClick === "function") onItemClick();
	};

	return (
		<img src={src} alt={alt} onClick={onClick} style={{cursor:"pointer"}}/>
	);
}

export default OpenModalImageItem;
