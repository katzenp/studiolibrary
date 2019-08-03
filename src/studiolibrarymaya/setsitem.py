# Copyright 2019 by Kurt Rathjen. All Rights Reserved.
#
# This library is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Lesser General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version. This library is distributed in the 
# hope that it will be useful, but WITHOUT ANY WARRANTY; without even the 
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.

import os

try:
    import mutils
except ImportError as error:
    print(error)

from studiolibrarymaya import baseitem


def save(path, *args, **kwargs):
    """Convenience function for saving a SetsItem."""
    SetsItem(path).save(*args, **kwargs)


def load(path, *args, **kwargs):
    """Convenience function for loading a SetsItem."""
    SetsItem(path).load(*args, **kwargs)


class SetsItem(baseitem.BaseItem):

    Name = "Selection Set"
    Extension = ".set"
    IconPath = os.path.join(os.path.dirname(__file__), "icons", "selectionSet.png")
    TransferClass = mutils.SelectionSet
    TransferBasename = "set.json"

    def loadFromCurrentOptions(self):
        """Load the selection set using the settings for this item."""
        namespaces = self.namespaces()
        self.load(namespaces=namespaces)

    def load(self, namespaces=None):
        """
        :type namespaces: list[str] | None
        """
        self.selectContent(namespaces=namespaces)

    def save(self, objects, **kwargs):
        """
        Save all the given object data to the item path on disc.

        :type objects: list[str]
        :type kwargs: dict
        """
        super(SetsItem, self).save(objects, **kwargs)

        # Save the selection set to the given path
        mutils.saveSelectionSet(
            self.path() + "/set.json",
            objects,
            metadata={"description": kwargs.get("comment", "")}
        )
