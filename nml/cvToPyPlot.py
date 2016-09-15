import cv2


def cv_to_pyplot(cvimg):
    b, g, r = cv2.split(cvimg)
    py_plot_img = cv2.merge([r, g, b])
    return py_plot_img
