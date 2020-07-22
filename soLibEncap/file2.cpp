#include "file2.h"

void File2::showImg(char *path)
{
    cv::Mat img = cv::imread(path);
    cv::namedWindow(path, CV_WINDOW_NORMAL);
    cv::resizeWindow(path, 500, 500);
    cv::imshow(path, img);
    cv::waitKey(0);
}